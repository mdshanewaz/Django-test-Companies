from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework import status, generics, viewsets
from rest_framework.decorators import api_view, action  
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse_lazy
import json
from .models import *
from .serializers import *

# Create your views here.

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @action(detail=True, methods=['get'])
    def employee(self, request, pk=None):
        try:
            company = Company.objects.get(pk=pk)
            companyEmployees = Employee.objects.filter(company=company)
            companyEmployeesSerializer = EmployeeSerializer(companyEmployees, many=True, context={'request':request})
            return Response(companyEmployeesSerializer.data)
        
        except Exception as e:
            print(e)
            return Response({
                "message": "Error || Company doesn't exist" 
            })


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

