from rest_framework import serializers
from .models import Users_table, shop
from django.contrib.auth.models import User
from rest_framework import serializers


class UsersTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users_table
        fields = '__all__'





class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = shop
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        return user
