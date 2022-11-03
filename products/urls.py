from django.urls import path
from . import views

urlpatterns = [
    path('category-2/', views.CategoryListAPIView.as_view()),
    path('products-2/', views.ProductListAPIView.as_view()),
    path('product-2-detail/<int:pk>/', views.ProductDetailAPIView.as_view()),
    path('rate-2/', views.RateAPIView.as_view())
]
