from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from storebackend.models import Category
from storebackend.serializers import CategorySerializer


# @api_view(['GET'])
# def demo(request):
#     queryset = Category.objects.all()
#     result = CategorySerializer(queryset, many=True)
#     return Response(result.data)


class CategoryView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # def post(self, request, *args, **kwargs):
    #     serializer = CategorySerializer(data=request.data)
    #     if serializer.is_valid():
    #         category = serializer.save()
    #         return Response(CategorySerializer(category).data)
    #     else:
    #         return Response(serializer.errors)
