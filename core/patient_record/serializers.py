from rest_framework import serializers
from accounts.models import CustomUser
from .models import Department, PatientRecords

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class PatientRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientRecords
        fields = '__all__'
