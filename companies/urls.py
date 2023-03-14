from django.contrib import admin
from django.urls import include, path
from .views import *
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('signup/', views.signup, name="signup")
]