from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from storebackend.models import User, Shop, Category, Product, ProductInfo, Parameter, ProductParameter, Contact, Order, \
    OrderItem


@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
    pass


@admin.register(Shop)
class ShopAdmin(ImportExportModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    pass
    # list_display = ['id', 'name']
    # search_fields = ['id', 'name']


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    pass
    # list_display = ['id', 'name', 'category']
    # search_fields = ['id', 'name', 'category']


@admin.register(ProductInfo)
class ProductInfoAdmin(ImportExportModelAdmin):
    pass


@admin.register(Parameter)
class ParameterAdmin(ImportExportModelAdmin):
    pass


@admin.register(ProductParameter)
class ProductParameterAdmin(ImportExportModelAdmin):
    pass


@admin.register(Contact)
class ContactAdmin(ImportExportModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    pass


@admin.register(OrderItem)
class OrderItemAdmin(ImportExportModelAdmin):
    pass
