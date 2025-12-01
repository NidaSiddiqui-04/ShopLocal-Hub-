from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from .views import *
 
app_name='accounts'


urlpatterns = [
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/',RegisterView.as_view(),name='Register_api'),
    path('api/profile/',ProfileView.as_view({'get': 'retrieve', 'put': 'update'}),name='profile_api'),
    path('',HomePage.as_view(),name="home_page"),
    path('login/',LoginPage.as_view(),name="login_page"),
    path('register/',RegisterPage.as_view(),name="register_page")
 ]