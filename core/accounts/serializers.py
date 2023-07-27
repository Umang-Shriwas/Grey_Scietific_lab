from rest_framework import serializers
from accounts.models import CustomUser
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from patient_record.serializers import *

class CustomUserSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()
    class Meta:
        model = CustomUser
        fields = ["id","email","name","user_type","department"]
    


class CustomUserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["email","name","user_type","password"]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = get_user_model()(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["email","name","user_type","department"]


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value