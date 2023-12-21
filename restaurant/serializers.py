from rest_framework import serializers
from .models import Menu, Booking
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User, Group
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['name', 'price', 'menu_item_description']
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
                
class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        extra_kwargs = {'reservation_slot': {'required': True}}

