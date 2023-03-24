from django.contrib import admin
from django.urls import include, path
from .views import *
from . import views
from rest_framework import routers 

router = routers.DefaultRouter()
router.register(r'company', CompanyViewSet)
router.register(r'employee', EmployeeViewSet)
router.register(r'asset', AssetViewSet)
router.register(r'devicelog', DeviceLogViewSet)

urlpatterns = [
    path('', views.login, name="login"),
    path('signup', views.signup, name="signup"),
    path('', include(router.urls)),
]