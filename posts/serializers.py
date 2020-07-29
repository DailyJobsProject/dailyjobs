from .models import Application, CompanyPost
from rest_framework import serializers

class CompanyPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyPost
        fields = ['user', 'title', 'description', 'created_at']


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['post', 'name', 'identifier']