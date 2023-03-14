from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signUp.html')

