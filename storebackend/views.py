from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from storebackend.models import Category
from storebackend.serializers import CategorySerializer


@api_view(['GET'])
def demo(request):
    queryset = Category.objects.all()
    result = CategorySerializer(queryset, many=True)
    return Response(result.data)

