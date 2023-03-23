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

class ResgisterSerializer(serializers.ModelSerializer):
    class Meta:
        models = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'password2')
        extra_kwargs = {
            'password' : {'write_only':True}
        }

    def save(self):
        user = User(
            username = self.validated_data['username'],
            email = self.validated_data['email'],
            first_name = self.validated_data['firstname'],
            last_name = self.validated_data['last_name'],
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise ValidationErr({'password': 'Password did not matched'})

        user.set_password(password)
        user.save()
        return user
    

