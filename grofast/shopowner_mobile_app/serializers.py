from admin_panel import serializers
from admin_panel.models import Category_table
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category_table
        fields = '__all__'