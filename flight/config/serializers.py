from rest_framework import serializers
from .models import Admins

class YourModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admins
        fields = '__all__'
