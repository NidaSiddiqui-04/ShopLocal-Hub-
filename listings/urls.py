from django import urls 
from django.urls import path
from .views import *
from django.contrib.auth import views as a_views

urlpatterns=[
    # path('post/',post_item),
    # path('post/<int:pk>/',post_item),
     path('post/',PostItem.as_view()),
     path('post/<int:pk>',PostItem.as_view()),
     path('api/dashboard/',Dashboard.as_view(),name="Dashboard_api"),
     path('dashboard/',DashboardView.as_view(),name="dashboard")


]