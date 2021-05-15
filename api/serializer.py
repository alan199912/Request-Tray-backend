from django.db.models import fields
from rest_framework import serializers
from . models import ApplyCreditUser

class ApplyCreditUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplyCreditUser
        fields = '__all__'