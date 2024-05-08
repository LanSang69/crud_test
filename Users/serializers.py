from rest_framework import serializers
from .models import User, Register_Method

#This file helps me make the model readable and accessible for my Angular frontend app

class RegisterMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register_Method
        fields = ['method']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'registered', 'f_name', 's_name', 'l_name', 'sl_name', 'email', 'password']