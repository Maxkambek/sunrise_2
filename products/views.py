from .models import Category_2, Product_2, Rate_2
from .serializers import Category2Serializer, Product2Serializer, Product2DetailSerializer, Rate2Serializer
from rest_framework import generics
from rest_framework.response import Response


class CategoryListAPIView(generics.ListAPIView):
    serializer_class = Category2Serializer
    queryset = Category_2.objects.all()


class ProductListAPIView(generics.ListAPIView):
    queryset = Product_2.objects.all()
    serializer_class = Product2Serializer

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
        serializer = Product2Serializer(queryset, many=True)
        return Response({'data': serializer.data, 'brands': lst})


class ProductDetailAPIView(generics.RetrieveAPIView):
    serializer_class = Product2DetailSerializer
    queryset = Product_2.objects.all()


class RateAPIView(generics.CreateAPIView):
    queryset = Rate_2.objects.all()
    serializer_class = Rate2Serializer
