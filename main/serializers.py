from .models import Product, ProductImage, Category, Attribute, Rate
from rest_framework.serializers import ModelSerializer


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name','image']


class ProductImageSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'product', 'image']


class AttributeSerializer(ModelSerializer):
    class Meta:
        model = Attribute
        fields = ['id', 'key', 'value']


class ProductSerializer(ModelSerializer):
    product_images = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'get_rate', 'name', 'product_images', 'category', 'brand', 'price', 'description']


class ProductDetailSerializer(ModelSerializer):
    product_images = ProductImageSerializer(many=True)
    attribute_product = AttributeSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'get_rate','name', 'category', 'brand', 'price', 'description', 'product_images', 'attribute_product']


class RateSerializer(ModelSerializer):
    class Meta:
        model = Rate
        fields = ['id', 'rate', 'product']
