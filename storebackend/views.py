from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from storebackend.models import Category, Product, Contact
from storebackend.serializers import CategorySerializer, ProductSerializer, ContactSerializer
from storebackend.services import read_yaml_write_to_db, create_user_data, confirm_user_email


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

    # def list(self, request, *args, **kwargs):
    #     return Response({'text': 'hello'})

    def create(self, request, *args, **kwargs):
        pass


class CategoryView(ListAPIView):
    """
    Класс для просмотра категорий товаров
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryCreateView(CreateAPIView):
    """
    Класс для создания категорий товаров
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

    # def post(self, request, *args, **kwargs):
    #     serializer = CategorySerializer(data=request.data)
    #     if serializer.is_valid():
    #         category = serializer.save()
    #         return Response(CategorySerializer(category).data)
    #     else:
    #         return Response(serializer.errors)


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
    permission_classes = [AllowAny]  # Задать согласно аутентификации поставщика!!!!

    def post(self, request, *args, **kwargs):
        return read_yaml_write_to_db(request, *args, **kwargs)

