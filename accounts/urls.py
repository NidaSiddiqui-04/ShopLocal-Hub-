from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from .views import *

urlpatterns = [
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/',RegisterView.as_view(),name='Register_api'),
    path('api/profile',ProfileView.as_view({'get': 'retrieve', 'put': 'update'}),name='profile_api'),
 ]