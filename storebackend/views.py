from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from storebackend.models import Category, Product, Contact
from storebackend.serializers import CategorySerializer, ProductSerializer, ContactSerializer
from storebackend.services import read_yaml_write_to_db, create_user_data, confirm_user_email, error_prompt


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
            return error_prompt(False, f'Please check: user_id', 400)

    def retrieve(self, request, *args, **kwargs):
        if request.data['user'] == request.user.id:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        else:
            return error_prompt(False, f'Please check: user_id', 400)

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
            return error_prompt(False, f'Please check: user_id', 400)

    def destroy(self, request, *args, **kwargs):
        if request.data['user'] == request.user.id:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return error_prompt(False, f'Please check: user_id', 400)

    def list(self, request, *args, **kwargs):
        # queryset = self.filter_queryset(self.get_queryset())
        queryset = Contact.objects.filter(user_id=request.user.id)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


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
    Класс для просмотра категорий товаров
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateView(CreateAPIView):
    """
    Класс для создания категорий товаров
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]


class SupplierCreateView(CreateAPIView):
    """
    Класс для создания/обновления данных поставщика
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        if request.data['user_id'] == str(request.user.id):
            return read_yaml_write_to_db(request, *args, **kwargs)
        else:
            return error_prompt(False, f'Please check: user_id', 400)
