from rest_framework import serializers
from companies.models import *
from django import forms

class DeviceLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceLog
        fields = 'checked_in_condition'
    

