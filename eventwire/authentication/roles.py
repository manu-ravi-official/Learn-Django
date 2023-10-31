from django.db import models
from rest_framework.exceptions import APIException
from eventwire.error_codes import ROLE_ACCESS_DENIED
from rest_framework.permissions import BasePermission


class RoleAccessDenied(APIException):
    status_code = 403
    default_detail = ROLE_ACCESS_DENIED


class IsModeratorUser(BasePermission):

    def has_permission(self, request, view):
        if request.user.role == UserRoles.MODERATOR:
            return True
        else:
            raise RoleAccessDenied()


class IsUser(BasePermission):

    def has_permission(self, request, view):
        if request.user.role == UserRoles.USER:
            return True
        else:
            return False


class IsEmployee(BasePermission):

    def has_permission(self, request, view):
        if request.user.role == UserRoles.EMPLOYEE:
            return True
        else:
            return False


class UserRoles(models.TextChoices):
    ADMIN = 1, 'Admin'
    MODERATOR = 2, 'Moderator',
    USER = 3, 'User'
    EMPLOYEE = 4, 'Employee'
