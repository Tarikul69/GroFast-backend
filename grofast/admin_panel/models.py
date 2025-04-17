from django.contrib.auth.models import AbstractUser
from django.db import models

class Users_table(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    password = models.CharField(max_length=128)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.username

class shop(models.Model):
    shop_id = models.AutoField(primary_key=True)
    shop_name = models.CharField(max_length=255)
    shop_address = models.TextField()
    shop_phone_number = models.CharField(max_length=20, blank=True, null=True)
    shop_type = models.CharField(max_length=50, choices=[('grocery', 'Grocery'), ('electronics', 'Electronics'), ('clothing', 'Clothing')])
    shop_status = models.CharField(max_length=20, choices=[('active', 'Active'), ('inactive', 'Inactive')])
    shop_condition = models.CharField(max_length=20, choices=[('new', 'New'), ('used', 'Used')])
    shop_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.username