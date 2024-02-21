from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from storebackend.models import Category
from storebackend.serializers import CategorySerializer


@api_view(['GET'])
def demo(request):
    queryset = Category.objects.all()
    result = CategorySerializer(queryset, many=True)
    return Response(result.data)


class CategoryView(APIView):

    def get(self, request, *args, **kwargs):
        queryset = Category.objects.all()
        result = CategorySerializer(queryset, many=True)
        return Response(result.data)

    def post(self, request, *args, **kwargs):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            shop = serializer.save()
            return Response(CategorySerializer(shop).data)
        else:
            return Response(serializer.errors)
