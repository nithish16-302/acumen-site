from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.acuthon, name='acuthon'),
    path('/register', views.register, name='acuthon_register'),
    path('/login', views.login, name='acuthon_login'),
    path('/teams', views.teams, name='acuthon_teams')
]