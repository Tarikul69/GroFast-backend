from rest_framework import serializers
from .models import Users_table, shop

class UsersTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users_table
        fields = '__all__'





class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = shop
        fields = '__all__'