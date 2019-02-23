from django.urls import path, include

from . import views
app_name = 'acuthon'
urlpatterns = [
    path('', views.acuthon, name='acuthon'),
    path('/register', views.register, name='acuthon_register'),
    path('/login', views.login_view, name='acuthon_login'),
    path('/teams', views.teams, name='acuthon_teams'),
    path('/logout',views.logout_view,name='acuthon_logout'),
    path('/pay',views.payment_request,name='acuthon_pay'),
    path('/payment_response',views.payment_response, name='acuthon_pay_response'),
    path('/payment_webhook',views.payment_webhook, name='acuthon_pay_webhook')
]