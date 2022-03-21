from django.shortcuts import render
from rest_framework import viewsets
from mainapp.models import User
from mainapp.serializers import RegisterSerializer, UserSerializer, TokenSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.forms import model_to_dict

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny, )


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TokenView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('pk', None)
        token = Token.objects.get(user_id=user_id)
        return Response({"token": token.key})
        