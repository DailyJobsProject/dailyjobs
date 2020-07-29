from rest_framework import serializers
from .models import Company, Employee, User

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['user', 'name', 'telephone', 'about', 'image']

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['user', 'first_name', 'last_name', 'telephone', 'about', 'image', 'cv']
