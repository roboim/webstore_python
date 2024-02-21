from django.urls import path

from storebackend.views import CategoryView

app_name = 'storebackend'

urlpatterns = [
    path('categories/', CategoryView.as_view(), name='categories'),
]
