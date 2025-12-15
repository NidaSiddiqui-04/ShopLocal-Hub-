from .serializers import PostItemSerializer
from rest_framework.views import APIView, View
from django.views.generic.base import TemplateView

class AboutUs(TemplateView):
    template_name = 'aboutus.html'
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.exceptions import PermissionDenied
from rest_framework.parsers import MultiPartParser, FormParser
from .models import ItemsForSale
from rest_framework.mixins import ListModelMixin
from rest_framework.generics import GenericAPIView


# function based view (APIView)
# @api_view(["GET","POST","PUT","DELETE"])
# def post_item(request,pk=None):
#     if request.method=="GET":
#         items=ItemsForSale.objects.all()
#         serilalizer=PostItemSerializer(items,many=True)
#         return Response(serilalizer.data)
    

#     if request.method=="POST":
    
#         serilalizer=PostItemSerializer(data=request.data)
#         if serilalizer.is_valid():
    
#             serilalizer.save(user=request.user)
#             return Response(serilalizer.data,status=status.HTTP_201_CREATED)
#         return Response(serilalizer.errors,status=status.HTTP_400_BAD_REQUEST)
    

#     if request.method=="PUT":
#         id =pk
#         items=ItemsForSale.objects.get(pk=id)
#         serilalizer=PostItemSerializer(items,request.data,partial=True)
#         if serilalizer.is_valid():
#             serilalizer.save()
#             return Response(serilalizer.data,status=status.HTTP_201_CREATED)
#         return Response(serilalizer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method=="DELETE":
#         id=pk
#         items=ItemsForSale.objects.get(id=id)
#         items.delete()
#         return Response({'msg':'deleted'})


# class based (APIView)

class PostItem(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request,pk=None):
        id =pk
        if id is not None:
            items=ItemsForSale.objects.get(id=id)
            serializer=PostItemSerializer(items)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            items=ItemsForSale.objects.all()
            serializer=PostItemSerializer(items,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        

    def post(self,request):
        serializer=PostItemSerializer(data=request.data)  
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk):
        id=pk
        items=ItemsForSale.objects.get(id=id)
        serializer=PostItemSerializer(items,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors)
    
    def delete(self,request,pk):
        id=pk
        items=ItemsForSale.objects.get(id=id)
        items.delete()
        return Response({'msg': 'item deleted successfully'})
    

# dashboard  using GENERICAPIView and model mixin


class Dashboard(GenericAPIView,ListModelMixin):
    
    queryset=ItemsForSale.objects.all()
    serializer_class=PostItemSerializer
    
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    

class DashboardView(TemplateView):
    template_name='listings/dashboard.html'