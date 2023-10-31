from .models import CustomUser
from rest_framework import serializers
from eventwire.error_codes import *
from .roles import UserRoles
class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(allow_blank=True, required=False)
    first_name = serializers.CharField(max_length=30, allow_blank=True)
    last_name = serializers.CharField(max_length=30, allow_blank=True, required=False)
    address = serializers.CharField(max_length=255, allow_blank=True, required=False)
    phone_number = serializers.CharField(max_length=15, allow_blank=True, required=False)
    age = serializers.IntegerField(allow_null=True, required=False)
    role = serializers.CharField(required=False)
    # groups = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all(), many=True)
    # user_permissions = serializers.PrimaryKeyRelatedField(queryset=Permission.objects.all(), many=True)

    class Meta:
        model = CustomUser
        fields = [
            'email',
            'first_name',
            'last_name',
            'address',
            'phone_number',
            'age',
            'password',
            'role'

        ]

    def validate_first_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError(ERROR_NAME_TOO_SHORT)
        return value
