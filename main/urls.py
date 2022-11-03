from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.CategoryListAPIView.as_view()),
    path('products/', views.ProductListAPIView.as_view()),
    path('product-detail/<int:pk>/', views.ProductDetailAPIView.as_view()),
    path('rate/', views.RateAPIView.as_view())
]
