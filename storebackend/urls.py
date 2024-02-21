from django.urls import path

from storebackend.views import CategoryView, CategoryCreateView, ProductView, ProductCreateView

app_name = 'storebackend'

urlpatterns = [
    path('categories/', CategoryView.as_view(), name='categories'),
    path('categories/create/', CategoryCreateView.as_view(), name='categories_creating'),
    path('products/', ProductView.as_view(), name='products'),
    path('products/create/', ProductCreateView.as_view(), name='products_creating'),
]
