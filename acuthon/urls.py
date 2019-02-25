from django.urls import path, include

from . import views
app_name = 'acuthon'
urlpatterns = [
    path('', views.acuthon, name='acuthon'),
    path('/register', views.register, name='acuthon_register'),
    path('/login', views.login_view, name='acuthon_login'),
    path('/participant', views.participant, name='acuthon_participant'),
    path('/team', views.team, name='acuthon_team_create'),
    path('/team/create', views.team_create, name='acuthon_team_create'),
    path('/team/join', views.team_join, name='acuthon_team_join'),
    path('/logout',views.logout_view,name='acuthon_logout'),
    path('/pay',views.payment_request,name='acuthon_pay'),
    path('/payment_response',views.payment_response, name='acuthon_pay_response'),
    path('/payment_webhook',views.payment_webhook, name='acuthon_pay_webhook')
]