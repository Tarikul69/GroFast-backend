from rest_framework import serializers
from .models import Category_table, Users_table, shop
from django.contrib.auth.models import User
 

class UsersTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users_table
        fields = '__all__'
        depth = 1

class ShopSerializer(serializers.ModelSerializer):
    shop_rating = serializers.FloatField(default=0.00)
    class Meta:
        model = shop
        fields = '__all__'
      

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category_table
        fields = '__all__'
        depth = 1

 