from django.shortcuts import render
from .serializers import ItemsSerializer
from rest_framework.views import APIView
from .models import ItemsForSale
from rest_framework.permissions import IsAuthenticated
# Create your views here.



class items(APIView):
    serializer_class=ItemsSerializer
    permission_classes=[IsAuthenticated]
    
    def get_queryset(self):
        return ItemsForSale.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)