from .models import Category, Product, Rate
from .serializers import CategorySerializer, ProductSerializer, ProductDetailSerializer, RateSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class CategoryListAPIView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        pk = self.request.GET.get('pk')
        min_p = self.request.GET.get('min_p')
        max_p = self.request.GET.get('max_p')
        brand = self.request.GET.get('brand')
        lst = {}
        if pk:
            queryset = queryset.filter(category_id=pk)
            for i in queryset:
                if i not in lst:
                    lst[i.id] = i.brand
        if brand:
            queryset = queryset.filter(brand__icontains=brand)
        if min_p:
            queryset = queryset.filter(price__gte=min_p)
        if max_p:
            queryset = queryset.filter(price__lte=max_p)
        serializer = ProductSerializer(queryset, many=True)
        return Response({'data': serializer.data, 'brands': lst})


class ProductDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()


class RateAPIView(generics.CreateAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
