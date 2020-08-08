from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import UserSerializers,LoginSerializer
from rest_framework import status
from rest_framework.response import Response
from django.contrib import auth
from django.conf import settings
import jwt

class RegisterView(GenericAPIView):
    serializer_class=UserSerializers
    def post(self,request):
        Serializers=UserSerializers(data=request.data)
        if Serializers.is_valid():
            Serializers.save()
            return Response(Serializers.data,status=status.HTTP_201_CREATED)
        return Response(Serializers.errors,status=status.HTTP_400_BAD_REQUEST)

class LoginView(GenericAPIView):
    serializer_class=LoginSerializer
    def post(self,request):
        data=request.data
        username=data.get('username','')
        password=data.get('password','')
        user=auth.authenticate(username=username,password=password)
        if user:
            auth_token=jwt.encode({
                'username':user.username
            },settings.JWT_SECRET_KEY)
            serializer=UserSerializers(user)
            data={
                'user':serializer.data,'token':auth_token
            }
            return Response(data,status=status.HTTP_200_OK)
        return Response({'detail':'Invalid credentials'},status=status.HTTP_401_UNAUTHORIZED)   

