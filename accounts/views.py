from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import AllowAny,IsAuthenticated
from .serializers import RegisterSerializer,UserProfileSerializer
from django.contrib.auth import get_user_model
from rest_framework import response,status
from rest_framework import generics
# Create your views here

class RegisterView(generics.CreateAPIView):
    serializer_class=RegisterSerializer
    permission_classes=[AllowAny]

    
class ProfileView(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated]
    serializer_class=UserProfileSerializer


    def get_object(self):
        return self.request.user
