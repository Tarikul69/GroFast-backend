from rest_framework import serializers
from .models import Users_table

class UsersTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users_table
        fields = '__all__'