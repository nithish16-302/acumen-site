from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *


# Create your views here.
def acuthon(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        print(request.POST)
        return HttpResponse('POST called'+str(request.POST))
    elif request.method == 'GET':
        return render(request, 'registration.html')
        

def login(request):
    if request.method == 'POST':
        user = User.objects.create_user(**request.POST)
    elif request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('acuthon')
        else:
            return render(request, 'login.html')
        

@login_required(login_url='/acuthon/login/')
def teams(request):
    if request.method == 'POST':
        return HttpResponse('POST called')
    elif request.method == 'GET':
        return HttpResponse('GET called')
        