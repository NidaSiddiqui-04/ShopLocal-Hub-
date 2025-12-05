from .serializers import PostItemImageSerializer ,PostItemSerializer
from rest_framework.views import APIView, View
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .models import ItemsForSale,ItemImage
from rest_framework.exceptions import PermissionDenied
from rest_framework.parsers import MultiPartParser, FormParser




class PostItem(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PostItemSerializer(data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
