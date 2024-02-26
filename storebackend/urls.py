from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenBlacklistView,
)

from storebackend.views import UserCreateView, CategoryView, CategoryCreateView, ProductView, ProductCreateView, \
    SupplierCreateView, UserConfirmView

app_name = 'storebackend'

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('user/create/', UserCreateView.as_view(), name='user-create'),
    path('user/create/confirm/', UserConfirmView.as_view(), name='user-confirm'),
    path('categories/', CategoryView.as_view(), name='categories'),
    path('categories/create/', CategoryCreateView.as_view(), name='categories-create'),
    path('products/', ProductView.as_view(), name='products'),
    path('products/create/', ProductCreateView.as_view(), name='products-create'),
    path('supplier/data/', SupplierCreateView.as_view(), name='supplier-data'),
]
