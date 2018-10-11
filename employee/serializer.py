from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    """
        This serializer serializes the Employee data
    """
    class Meta:
        model = Employee
        fields = ("name", "designation")

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.designation = validated_data.get("designation", instance.designation)
        instance.save()
        return instance


class TokenSerializer(serializers.Serializer):
    """
    This serializer serializes the token data
    """
    token = serializers.CharField(max_length=255)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email")
