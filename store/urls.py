from django.urls import path, include
from .views import *

urlpatterns = [
    path('category/', Categorycreateview.as_view(),name='category'),
    path('products/', Productcreateview.as_view(), name='product'),
    path('products/<int:pk>/', Productdetails.as_view(), name='product-detail'),
    path('customer/',Customercreateview.as_view(),name='customer_detail'),
    path('customer/<int:pk>/', Customerdetails.as_view(), name='customer_detail'),

]
