from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from .roles import UserRoles


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        extra_fields = {
            'is_staff': True,
            'is_superuser': True,
        }
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    age = models.PositiveIntegerField(null=True, blank=True)
    groups = models.ManyToManyField(Group, related_name='customUser_set')
    user_permissions = models.ManyToManyField(Permission, related_name='customUser_set')
    is_staff=models.BooleanField(default=False)
    role = models.CharField(max_length=20, default='attendee')
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    def __str__(self):
        return self.email
