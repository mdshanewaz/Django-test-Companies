from django.shortcuts import render

from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework import status  
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import *
from .serializers import *

# Create your views here.

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signUp.html')

class CompanyListView(ListAPIView):
    queryset = Company.objects.all()
    model = Company
    template_name = 'company_list.html'

class EmployeeCreateView(CreateAPIView):
    model = Employee
    fields = ['name', 'email', 'job_title', 'company']
    template_name = 'employee_create.html'
    success_url = reverse_lazy('company_list')

class AssetListView(ListAPIView):
    model = Asset
    template_name = 'asset_list.html'

class DeviceLogCreateView(CreateAPIView):
    model = DeviceLog
    fields = ['asset', 'employee', 'checked_out_condition']
    template_name = 'device_log_create.html'
    success_url = reverse_lazy('asset_list')

class DeviceLogUpdateView(UpdateAPIView):
    template_name = 'device_log_update.html'

    def form_valid(self, form):
        device_log = self.object
        asset = device_log.asset
        asset.condition = form.cleaned_data.get('checked_in_condition')
        asset.save()
        device_log.checked_in_date = timezone.now()
        return super().form_valid(form)
