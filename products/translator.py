from .models import Category_2, Product_2, Attribute_2
from modeltranslation.translator import register, TranslationOptions


@register(Category_2)
class CategoryTranslation(TranslationOptions):
    fields = ('name',)


@register(Product_2)
class ProductTranslation(TranslationOptions):
    fields = ['name', 'description']


@register(Attribute_2)
class AttributeTranslation(TranslationOptions):
    fields = ('key', 'value')
