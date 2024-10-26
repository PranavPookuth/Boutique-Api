from django.shortcuts import render
from rest_framework import generics,status
from . serializers import CategorySerializer,ProductSerializer
from . models import Category,Product


# Create your views here.
class Categorycreateview(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class Productcreateview(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class Productdetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer