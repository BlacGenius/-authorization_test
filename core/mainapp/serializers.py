from lib2to3.pgen2 import token
from rest_framework import serializers
from mainapp.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class TokenSerializer(serializers.ModelSerializer):
    class MEta:
        model = Token
        fields = ('user', 'key', 'created')


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'password')
        extra_kwargs = {
            "password": {"write_only": True}
        }
    
    def create(self, validated_data):
        user = User.objects.create(
            email = validated_data['email']
            )
        user.set_password(validated_data['password'])
        user.is_active = True
        user.save()
        if user in User.objects.all():
            self.create_token(user)
        return user
    
    def create_token(self, user):
        token = Token.objects.create(user=user)
        return token

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('email', 'username', 'about',)
        read_only_fields = ('email', 'username', 'about',)