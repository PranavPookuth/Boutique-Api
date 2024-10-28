from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        category_data = validated_data.pop('category')

        category, created = Category.objects.get_or_create(**category_data)
        product = Product.objects.create(category=category, **validated_data)
        return product

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model =Customer
        fields='__all__'

class OrderSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(source='customer.customer_name',read_only=True)
    # p_name=serializers.CharField(source='product.product_name',read_only=True)
    class Meta:
        model = Order
        fields = '__all__'
