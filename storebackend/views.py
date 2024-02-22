from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from storebackend.models import Category, Product
from storebackend.serializers import CategorySerializer, ProductSerializer


# @api_view(['GET'])
# def demo(request):
#     queryset = Category.objects.all()
#     result = CategorySerializer(queryset, many=True)
#     return Response(result.data)


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


        return Response({'Status': True, 'success': 'Yes'}, status=201)
        # return self.create(request, *args, **kwargs)

