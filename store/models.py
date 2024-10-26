from django.db import models

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=200)

class Customer(models.Model):
    customer_name=models.CharField(max_length=100)
    email=models.EmailField()
    def __str__(self):
        return self.customer_name


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()
    image=models.ImageField(upload_to='Image')

    def __str__(self):
        return self.product_name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer

