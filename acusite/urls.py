from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('events/', views.events, name='events'),
    path('map3d/', views.map3d, name='map3d'),
    path('registration', views.registration, name='registration'),
    path('register', views.register, name='register'),
    path('sponsers', views.sponsers, name='sponsers'),
    path('team', views.team, name='team'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('eventreg/', views.event_reg, name="eventsreg"),
    path('eventdel', views.event_del, name="eventdel"),
    path('change_registration_details/', views.change_details, name="change"),
    path('forgotpwd/', views.forgotpwd, name="forgotpwd"),
    path('otpgenerator/', views.otpgenerator, name="otpgenerator"),
    path('otpcomparator',views.otpcomparator,name = 'otpcomparator'),
    path('changepwd', views.changepwd, name='changepwd'),
    path('change_registration_details/', views.change_details, name="change"),
    path('payment_request/', views.payment_request, name="payment_request"),
    path('payment_response/<slug:event>/', views.payment_response, name="payment_response"),
    path('gallery', views.gallery, name="gallery"),
    path('map3dHome', views.map3dHome, name="map3dHome"),

]