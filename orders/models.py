from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.

class Order(models.Model):
    STATUS_CHOICES = [
    ('ordered', 'Ordered'),
    ('processing', 'Processing'),
    ('shipped', 'Shipped'),
    ('delivered', 'Delivered'),
    ('cancelled', 'Cancelled'),
]

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    total_price=models.DecimalField(max_digits=10, decimal_places=2)
    full_name=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    address=models.TextField()
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pincode=models.CharField(max_length=10)
    status=models.CharField(max_length=20,choices=STATUS_CHOICES, default='ordered')
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items')
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    price=models.DecimalField(max_digits=10,decimal_places=2)

    def subtotal(self):
        return self.price * self.quantity

