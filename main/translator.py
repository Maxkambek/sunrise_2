from .models import Category, Product, Attribute
from modeltranslation.translator import register, TranslationOptions


@register(Category)
class CategoryTranslation(TranslationOptions):
    fields = ('name',)


@register(Product)
class ProductTranslation(TranslationOptions):
    fields = ['name', 'description']


@register(Attribute)
class AttributeTranslation(TranslationOptions):
    fields = ('key', 'value')
