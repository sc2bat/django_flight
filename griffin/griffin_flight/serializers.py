from rest_framework import serializers
from .models import Admins, Books, Airplanes, Airports, Flights, Passports, Users
from django.contrib.auth.models import User, Group

class AdminsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admins
        fields = ['admin_id', 'admin_name', 'email', 'created_at', 'is_deleted']

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'
        
class AirplanesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplanes
        fields = '__all__'

class AirportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airports
        fields = '__all__'

class FlightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flights
        fields = '__all__'

class PassportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passports
        fields = '__all__'

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['user_id', 'user_name', 'email', 'created_at', 'is_deleted']

# auth serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', "first_name", "last_name")

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("name", )