from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from storebackend.models import Category, Product


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['id', 'name']


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ['id', 'name', 'category']
    search_fields = ['id', 'name', 'category']

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     pass


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     pass
