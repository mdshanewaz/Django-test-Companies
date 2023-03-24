from rest_framework import status, serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from companies.models import *
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from xml.dom import ValidationErr

# create Serializers

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Company
        fields = "__all__"

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Employee
        fields = "__all__"

class AssetSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Asset
        fields = "__all__"

class DeviceLogSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = DeviceLog
        fields = "__all__"

    

