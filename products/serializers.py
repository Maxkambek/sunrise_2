from .models import Product_2, ProductImage_2, Category_2, Attribute_2, Rate_2
from rest_framework.serializers import ModelSerializer


class Category2Serializer(ModelSerializer):
    class Meta:
        model = Category_2
        fields = ['id', 'name', 'image']


class Product2ImageSerializer(ModelSerializer):
    class Meta:
        model = ProductImage_2
        fields = ['id', 'product', 'image']


class Attribute2Serializer(ModelSerializer):
    class Meta:
        model = Attribute_2
        fields = ['id', 'key', 'value']


class Product2Serializer(ModelSerializer):
    product_2_images = Product2ImageSerializer(many=True)

    class Meta:
        model = Product_2
        fields = ['id', 'name', 'product_2_images', 'category', 'brand', 'price', 'description']


class Product2DetailSerializer(ModelSerializer):
    product_2_images = Product2ImageSerializer(many=True)
    attribute_product = Attribute2Serializer(many=True)

    class Meta:
        model = Product_2
        fields = ['id', 'get_rate','name', 'category', 'brand', 'price', 'description', 'product_2_images', 'attribute_product']


class Rate2Serializer(ModelSerializer):
    class Meta:
        model = Rate_2
        fields = ['id', 'rate', 'product']
