from .models import Event, EventImage
from rest_framework import serializers
from eventwire.error_codes import *
from .models import EventImage


class EventImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventImage
        fields = ['image']


class EventSerializer(serializers.ModelSerializer):
    image = EventImageSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ['name', 'image']

    def validate_name(self, value):

        if not value:
            raise serializers.ValidationError(ERROR_NAME_EMPTY)

        if not value.isalpha():
            raise serializers.ValidationError(ERROR_NAME_NOT_ALPHABETIC)

        if len(value) > 255:
            raise serializers.ValidationError(ERROR_NAME_TOO_LONG)

        if len(value) < 3:
            raise serializers.ValidationError(ERROR_NAME_TOO_SHORT)
        return value
