from django.urls import path
from rest_framework import routers
from .views import CustomEventCreate
from rest_framework.permissions import IsAdminUser
router = routers.DefaultRouter()
urlpatterns = [
    path('create-event/', CustomEventCreate.as_view(), name='custom_event_create'),
]