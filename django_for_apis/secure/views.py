from rest_framework import generics
from django.shortcuts import render
from rest_framework.views import APIView

from rest_framework import status
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response

from django.contrib.auth import authenticate

# Create your views here.
from .serializers import UserSerializer

class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer

class LoginView(APIView):
    permission_classes = ()
    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return JsonResponse({"token": user.auth_token.key})
        else:
            return JsonResponse({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)