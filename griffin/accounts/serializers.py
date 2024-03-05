from django.contrib.auth.models import User, Group
from .models import Users
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', "first_name", "last_name")

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['user_id', 'user_name', 'email', 'created_at', 'is_deleted']