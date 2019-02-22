from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *


# Create your views here.
#All get related links are displayed in acuthon itself using modals or some divs
#All other views are just for handling POST data
def acuthon(request):
    return render(request, 'index.html')

def register(request):
    """
    POST:
    Create a User
    After successful user creation create participant
    Get the extra details needed for participant model
    Commit the changes and data to DB
    Login the user
    """
    if request.method == 'POST':
        print(request.POST)
        return HttpResponse('POST called'+str(request.POST))
        

def login(request):
    """
    POST:
    Check if the credentials are correct then login the user
    """
    if request.method == 'POST':
        user = User.objects.create_user(**request.POST)
        

@login_required(login_url='/acuthon/login/')
def teams(request):
    """
    POST:
    Create team and add participants as CSV
    """
    if request.method == 'POST':
        return HttpResponse('POST called')
    elif request.method == 'GET':
        return HttpResponse('GET called')
        