from django.db.models import F, Q
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from storebackend.models import Category, Product, Contact, Shop, Order, OrderItem, ProductInfo, STATE_CHOICES
from storebackend.serializers import CategorySerializer, ProductSerializer, ContactSerializer, OrderSerializer, \
    ProductDataSerializer
from storebackend.services import read_yaml_write_to_db, create_user_data, confirm_user_email, error_prompt, \
    create_shop_order
from storebackend.signals import new_order


# @api_view(['GET'])
# def demo(request):
#     queryset = Category.objects.all()
#     result = CategorySerializer(queryset, many=True)
#     return Response(result.data)

class UserCreateView(CreateAPIView):
    """
    Создать пользователя
    """
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        return create_user_data(request, *args, **kwargs)


class UserConfirmView(APIView):
    """
    Подтвердить почтовый адрес пользователя
    """

    def post(self, request, *args, **kwargs):
        return confirm_user_email(request, *args, **kwargs)


class UserContactView(ModelViewSet):
    """
    Создание и редактирование контактов пользователя
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if request.data['user'] == request.user.id:
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return error_prompt(False, f'Please check: user_id', 401)

    def retrieve(self, request, *args, **kwargs):
        if request.data['user'] == request.user.id:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        else:
            return error_prompt(False, f'Please check: user_id', 401)

    def update(self, request, *args, **kwargs):
        if request.data['user'] == request.user.id:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                # If 'prefetch_related' has been applied to a queryset, we need to
                # forcibly invalidate the prefetch cache on the instance.
                instance._prefetched_objects_cache = {}

            return Response(serializer.data)
        else:
            return error_prompt(False, f'Please check: user_id', 401)

    def destroy(self, request, *args, **kwargs):
        if request.data['user'] == request.user.id:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return error_prompt(False, f'Please check: user_id', 401)

    def list(self, request, *args, **kwargs):
        # queryset = self.filter_queryset(self.get_queryset())
        queryset = Contact.objects.filter(user_id=request.user.id)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CartView(APIView):
    """
    Класс для обработки корзины
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        Получить информацию по корзине
        """
        user_cart = OrderItem.objects.values('order_id', 'product_info_id', 'product_info_id__price',
                                             'quantity').filter(order_id__user_id=request.user.id,
                                                                order_id__state='cart').order_by('order_id').annotate(
            total_price=F('quantity') * F('product_info_id__price'))
        data = list(user_cart)
        total_cart = 0  # Так как 'price' - PositiveIntegerField
        for line in data:
            total_cart += int(line['total_price'])
        data.append({'total_cart': total_cart})
        return Response(data)

    def post(self, request, *args, **kwargs):
        """
        Создать заказ в корзине
        """
        user_id = request.user.id
        orders = request.data.get('orders')
        try:
            for order in orders:
                if len(order) > 1:
                    return error_prompt(False, f'Please use one shop in an order', 400)
                order_cur = Order.objects.create(user_id=user_id, state='cart')
                for shop in order:
                    for product in shop['products']:
                        prodinfo_cur = ProductInfo.objects.get(shop_id=shop['shop_id'],
                                                               product_id=product['product_id'])
                        order_item = OrderItem.objects.create(order_id=order_cur.id, product_info_id=prodinfo_cur.id,
                                                              quantity=product['quantity'])
            return Response({'Status': True, 'description': f'Создано заказов: {len(orders)}'}, status=200)
        except Exception as error:
            return error_prompt(False, f'Please check: {error}', 400)

    def put(self, request, *args, **kwargs):
        """
        Редактировать заказ в корзине
        """
        user_id = request.user.id
        orders = request.data.get('orders')
        edited_order_items = list()
        try:
            for order in orders:
                if len(order) > 2:
                    return error_prompt(False, f'Please use one shop in an order', 400)
                order_num = order[0]['order_id']
                order_cur = Order.objects.get(user_id=user_id, state='cart', id=order_num)
                order_shops = [order[i] for i in range(1, len(order))]
                for shop in order_shops:
                    for product in shop['products']:
                        result = OrderItem.objects.filter(order_id=order_cur.id,
                                                          product_info_id__product_id=int(
                                                              product['product_id'])).update(
                            quantity=int(product['quantity']))
                        new = False
                        #  Создать позицию в заказе, если она отсутствовала
                        if result == 0:
                            shop_ident = OrderItem.objects.filter(order_id=order_cur.id).first()
                            if shop_ident.product_info.shop_id != int(shop['shop_id']):
                                return error_prompt(False, {'successfull_adjustments': edited_order_items}, 400)
                            prodinfo_cur = ProductInfo.objects.get(shop_id=shop['shop_id'],
                                                                   product_id=product['product_id'])
                            order_item = OrderItem.objects.create(order_id=order_cur.id,
                                                                  product_info_id=prodinfo_cur.id,
                                                                  quantity=product['quantity'])
                            new = True
                        edited_order_items.append(
                            {'order_id': order_cur.id, 'product_id': int(product['product_id']),
                             'quantity': int(product['quantity']), 'new': new})
            return Response({'Status': True, 'description': f'Успешно изменены: {edited_order_items}.'}, status=200)
        except Exception as error:
            return error_prompt(False, f'Successfully Edited: {edited_order_items}. '
                                       f'Please check: {error}', 400)

    def delete(self, request, *args, **kwargs):
        """
        Удалить позиции заказа в корзине
        """
        user_id = request.user.id
        orders = request.data.get('orders')
        deleted_order_items = list()
        try:
            for order in orders:
                if len(order) > 2:
                    return error_prompt(False, f'Please use one shop in an order', 400)
                order_num = order[0]['order_id']
                order_cur = Order.objects.get(user_id=user_id, state='cart', id=order_num)
                order_shops = [order[i] for i in range(1, len(order))]
                for shop in order_shops:
                    for product in shop['products']:
                        OrderItem.objects.filter(order_id=order_cur.id,
                                                 product_info_id__product_id=int(product['product_id'])).delete()
                        deleted_order_items.append({order_cur.id: product['product_id']})
                #  Удалить заказ, если в нём не осталось позиций
                empty_order = OrderItem.objects.filter(order_id=order_cur.id)
                if len(empty_order) == 0:
                    Order.objects.filter(id=order_cur.id).delete()
                    deleted_order_items.append({'Заказ': order_cur.id})
            return Response({'Status': True, 'description': f'Успешно удалены: {deleted_order_items}.'}, status=200)
        except Exception as error:
            return error_prompt(False, f'Successfully Deleted: {deleted_order_items}. '
                                       f'Please check: {error}', 400)


class CategoryView(ListAPIView):
    """
    Класс для просмотра категорий товаров
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]


class CategoryCreateView(CreateAPIView):
    """
    Класс для создания категорий товаров
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]


class ProductView(ListAPIView):
    """
    Класс для просмотра товаров
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateView(CreateAPIView):
    """
    Класс для создания товаров
    """
    queryset = ProductInfo.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]


class ProductInfoView(APIView):
    """
    Класс для просмотра товаров
    """
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        """
        Вывести информацию по продуктам с возможными фильтрами 'shop_id' или 'category_id'
        """
        try:
            shop_id = request.query_params.get('shop_id')
            category_id = request.query_params.get('category_id')

            query = Q(shop__state=True)
            if shop_id:
                query = query & Q(shop_id=shop_id)
            if category_id:
                query = query & Q(product__category_id=category_id)

            queryset = ProductInfo.objects.filter(query).select_related('shop', 'product__category').prefetch_related(
                'product_parameters__parameter').distinct()
            serializer = ProductDataSerializer(queryset, many=True)
            return Response(serializer.data)

        except Exception as error:
            return error_prompt(False, f'Please check: {error}', 400)


class SupplierCreateView(CreateAPIView):
    """
    Класс для создания/обновления данных поставщика
    """
    permission_classes = [IsAuthenticated]

    @extend_schema(parameters=[
        OpenApiParameter(name='data', description='Additional information', required=True, type=dict),
        OpenApiParameter(name='files', description='upload_file', required=True, type=str)
    ], description='"upload_file" is name of file.'
                   'values = {"DB": "postgres", "OUT": "yaml", "user_id": "user_id"}. '
                   'files=files, data=values', methods=['POST'])
    @action(detail=True, methods=['post'])
    def post(self, request, *args, **kwargs):
        if request.data['user_id'] == str(request.user.id):
            return read_yaml_write_to_db(request, *args, **kwargs)
        else:
            return error_prompt(False, f'Please check: user_id', 400)


class SupplierRetrieveUpdate(APIView):
    """
    Класс для просмотра/обновления статуса работы поставщика
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        if request.user.type != 'shop':
            return error_prompt(False, f'Available only for shop', 400)
        try:
            shop = Shop.objects.get(id=kwargs['pk'], user_id=request.user.id)
            return Response({'Status': shop.state, 'description': f'{shop.name}'}, status=200)
        except Exception as error:
            return error_prompt(False, f'Please check: user_id or shop_id. {error}', 400)

    def patch(self, request, *args, **kwargs):
        if request.user.type != 'shop':
            return error_prompt(False, f'Available only for shop', 400)
        try:
            shop_id = kwargs['pk']
            state = bool(request.data.get('state'))
            Shop.objects.filter(id=shop_id, user_id=request.user.id).update(state=state)
            return Response({'Status': state, 'description': f'Shop id: {shop_id}'}, status=200)
        except Exception as error:
            return error_prompt(False, f'Please check: user_id or shop_id. {error}', 400)


class OrderView(ModelViewSet):
    """
    Класс для работы с заказом
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """
        Разместить заказ из корзины и указать контакт для связи
        **kwargs={
        'order_id': '' - номер заказа;
        'state': 'new' - статус размещения заказа;
        'contact_id': '' - номер контакта для связи.
        }
        """
        try:
            order_id = request.data.get('order_id')
            state = request.data.get('state')
            contact_id = request.data.get('contact_id')
            if state != 'new':
                return error_prompt(False, f'Please check state (not new)', 400)
            order_cur = Order.objects.get(id=int(order_id))
            if order_cur.state != 'cart':
                return error_prompt(False, f'Please contact admin user (order_s state is not "cart")', 400)
            elif order_cur.user_id != request.user.id:
                return error_prompt(False, f'Please check order_id', 401)
            contact_cur = Contact.objects.get(id=int(contact_id))
            if contact_cur.user_id != request.user.id:
                return error_prompt(False, f'Please check contact_id', 401)
            order_cur.contact_id = contact_cur.id
            order_cur.state = 'new'
            order_cur.save()
            # Сигнал о создании нового заказа
            new_order.send(sender=self.__class__, user_email=request.user.email,
                           user_first_name=request.user.first_name)
            return Response({'Status': True,
                             'description': f'Успешно размещён заказ: {order_id}. '
                                            f'Ожидайте письмо на адрес {request.user.email}'},
                            status=201)
        except Exception as error:
            return error_prompt(False, f'Please check: {error}', 400)

    def retrieve(self, request, *args, **kwargs):
        """
        Получить информацию по заказу:

        url: .../order/order_id/

        Response({'Status': True, 'description': data}, status=200)
        """
        try:
            # Загрузить продукцию из заказа
            order_cur = Order.objects.get(id=int(kwargs['pk']))
            if order_cur.user_id != request.user.id:
                return error_prompt(False, f'Please check order_id', 401)
            user_items = OrderItem.objects.values('product_info_id__external_id', 'product_info_id__model',
                                                  'product_info_id__price', 'quantity').filter(
                order_id=order_cur.id).annotate(total_price=F('quantity') * F('product_info_id__price'))
            data = list(user_items)
            # Добавить расчёт стоимости
            total_order = 0  # Так как 'price' - PositiveIntegerField
            for line in data:
                total_order += int(line['total_price'])
            data.append({'total_order': total_order})
            # Добавить информацию по контакту
            if order_cur.contact_id:
                queryset = Contact.objects.get(id=order_cur.contact_id)
                contact_data = ContactSerializer(queryset)
                data.append(contact_data.data)
            return Response({'Status': True, 'description': data}, status=200)
        except Exception as error:
            return error_prompt(False, f'Please check: {error}', 400)

    def update(self, request, *args, **kwargs):
        """
        Для покупателя:
        возможность отмены заказа  **kwargs={'state': 'canceled'},

        Для магазина:
        возможность изменения статуса заказа  **kwargs={'state': ''},
        - cart - в корзине;
        - new - новый;
        - confirmed - подтверждённый;
        - assembled - подготовленный к отправке;
        - sent - отправленный;
        - delivered - доставленный;
        - canceled - отменённый.
        """
        try:
            state = str(request.data.get('state'))
            if request.user.type == 'buyer':
                if state != 'canceled':
                    return error_prompt(False, f'Please check state (not canceled)', 400)
                order_cur = Order.objects.get(id=int(kwargs['pk']))
                if order_cur.state == 'canceled':
                    return error_prompt(False, f'The order {order_cur.id} already canceled',
                                        304)
                elif order_cur.state != 'cart' and order_cur.state != 'new':
                    return error_prompt(False, f''
                                               f'Please contact admin user (order_s state is not "cart" or "new")',
                                        400)

                elif order_cur.user_id != request.user.id:
                    return error_prompt(False, f'Please check order_id', 401)
                order_cur.state = state
                order_cur.save()
                return Response({'Status': True, 'description': f'Успешно отменён заказ: {order_cur.id}.'},
                                status=200)
            elif request.user.type == 'shop':
                # Формируем список возможных статусов из данных в models.py
                states_order = [STATE_CHOICES[el][0] for el in range(len(STATE_CHOICES))]

                order_cur = Order.objects.get(id=int(kwargs['pk']))
                #  Размещение заказа магазином с бронированием товаров
                if order_cur.state == 'new' and state == 'confirmed':
                    create_shop_order(request)
                    return Response({'Status': True,
                                     'description': f'Успешно размещён заказ {order_cur.id}.'
                                                    f'Товар забронирован.'},
                                    status=201)
                # Иные случаи
                order_data = OrderItem.objects.values('order_id', 'product_info_id',
                                                      'product_info_id__shop_id__user_id').filter(
                    product_info_id__shop_id__user_id=request.user.id).first()
                if order_data['product_info_id__shop_id__user_id'] != request.user.id:
                    return error_prompt(False, f'Please check order_id', 401)
                elif order_cur.state == 'canceled':
                    return error_prompt(False, f'The order {order_cur.id} already canceled',
                                        304)
                if state in states_order:
                    order_cur.state = state
                    order_cur.save()
                    return Response({'Status': True,
                                     'description': f'Успешно изменён статус заказа {order_cur.id} '
                                                    f'в значение {order_cur.state}.'},
                                    status=201)
                else:
                    return error_prompt(False, f'Please check state', 401)
        except Exception as error:
            return error_prompt(False, f'Please check: {error}', 400)

    def destroy(self, request, *args, **kwargs):
        """
        Метод запрещён.
        return error_prompt(False, f'Delete method is not allowed', 405)
        """
        return error_prompt(False, f'Delete method is not allowed', 405)

    def list(self, request, *args, **kwargs):
        """
        Вывести список заказов покупателя без товаров в корзине, для магазинов все обозначенные товары.
        return Response(data)
        """
        if request.user.type == 'buyer':
            user_orders = OrderItem.objects.values('order_id', 'product_info_id', 'product_info_id__price',
                                                   'quantity').filter(order_id__user_id=request.user.id).exclude(
                order_id__state='cart').order_by('order_id').annotate(
                total_price=F('quantity') * F('product_info_id__price'))
            data = list(user_orders)
            total_cart = 0  # Так как 'price' - PositiveIntegerField
            for line in data:
                total_cart += int(line['total_price'])
            data.append({'total_cart': total_cart})
            return Response(data)
        elif request.user.type == 'shop':
            shop_orders = OrderItem.objects.values('order_id', 'product_info_id', 'product_info_id__price',
                                                   'quantity').filter(
                product_info_id__shop_id__user_id=request.user.id).order_by('order_id').annotate(
                total_price=F('quantity') * F('product_info_id__price'))
            data = list(shop_orders)
            total_orders = 0  # Так как 'price' - PositiveIntegerField
            for line in data:
                total_orders += int(line['total_price'])
            data.append({'total_orders': total_orders})
            data.append(
                {'user_id': request.user.id, 'shop': request.user.shop.name, 'user_company': request.user.company})
            return Response(data)

        return error_prompt(False, f'Incorrect user_type', 401)
