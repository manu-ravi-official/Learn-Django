from django.urls import path
from rest_framework import routers
from .views import CustomModeratorCreate,CustomUserCreate,CustomEmployeeCreate,UserLogin

router = routers.DefaultRouter()
urlpatterns = [
     path('create-moderator/', CustomModeratorCreate.as_view(), name='custom_moderator_create'),
     path('create-user/', CustomUserCreate.as_view(), name='custom_user_create'),
     path('create-emp/', CustomEmployeeCreate.as_view(), name='custom_emp_create'),
     path('login/', UserLogin.as_view(), name='user_login')
]