from django.contrib import admin
from .models import Category_2, Product_2, ProductImage_2, Attribute_2, Rate_2
from modeltranslation.admin import TranslationAdmin, InlineModelAdmin
from modeltranslation import admin as a


class CategoryAdmin(TranslationAdmin):
    list_display = ['name']


class ProductImageAdmin(admin.TabularInline):
    model = ProductImage_2
    extra = 1


class AttributeAdmin(a.TranslationTabularInline):
    model = Attribute_2
    extra = 8


class ProductAdmin(TranslationAdmin):
    list_display = ['name', 'brand', 'category']
    inlines = [ProductImageAdmin, AttributeAdmin]


admin.site.register(Category_2, CategoryAdmin)
admin.site.register(Product_2, ProductAdmin)
