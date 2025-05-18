from django.contrib.auth.models import AbstractUser
from django.db import models


# User Model
class Users_table(models.Model):
    #users_id = models.AutoField(primary_key=True)
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

# Shop Model
class shop(models.Model):
    shop_id = models.AutoField(primary_key=True)
    shop_name = models.CharField(max_length=255)
    shop_address = models.TextField()
    shop_phone_number = models.CharField(max_length=20, blank=True, null=True)
    shop_type = models.CharField(max_length=50, choices=[('grocery', 'Grocery'), ('electronics', 'Electronics'), ('clothing', 'Clothing')])
    shop_status = models.CharField(max_length=20, choices=[('active', 'Open'), ('inactive', 'Close')])
    shop_condition = models.CharField(max_length=20, choices=[('new', 'New'), ('used', 'Used')])
    #shop_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

#Product table Model
class Product_table(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    product_quantity = models.IntegerField()
    shop_id = models.ForeignKey(shop, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name
    
#Category table Model
class Category_table(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255)
    shop_id = models.ForeignKey(shop, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name
 #review_table 
class Review_table(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users_table, on_delete=models.CASCADE)
    shop = models.ForeignKey(shop, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return f"Rating: {self.rating}"