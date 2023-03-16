from django.contrib import admin
from django.urls import include, path
from .views import *
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('signup/', views.signup, name="signup"),

    path('companies/', CompanyListView.as_view(), name='company_list'),
    path('employees/create/', EmployeeCreateView.as_view(), name='employee_create'),
    path('assets/', AssetListView.as_view(), name='asset_list'),
    path('device_logs/create/', DeviceLogCreateView.as_view(), name='device_log_create'),
    path('device_logs/<int:pk>/update/', DeviceLogUpdateView.as_view(), name='device_log_update'),
]