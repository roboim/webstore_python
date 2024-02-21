from django.urls import path

from storebackend.views import CategoryView, CategoryCreateView

app_name = 'storebackend'

urlpatterns = [
    path('categories/', CategoryView.as_view(), name='categories'),
    path('categories/create/', CategoryCreateView.as_view(), name='categories_creating'),
]
