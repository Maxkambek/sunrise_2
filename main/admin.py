from django.contrib import admin
from .models import Category, Product, ProductImage, Attribute, Rate
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class ProductImageAdmin(admin.TabularInline):
    model = ProductImage
    extra = 1


class AttributeAdmin(TranslationTabularInline):
    model = Attribute
    extra = 8


class ProductAdmin(TranslationAdmin):
    list_display = ['name', 'brand', 'category']
    inlines = [ProductImageAdmin, AttributeAdmin]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
