from django import urls 
from django.urls import path
from .views import *
from django.contrib.auth import views as a_views

urlpatterns=[
    path('create_post/',PostItem.as_view(),name="create_post"),
]