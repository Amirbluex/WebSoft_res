from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [

    path('login', views.UserLogin.as_view(), name='user_login'),
    path('logout', views.user_logout, name='user_logout'),
    path('register', views.UserRegister.as_view(), name='user_register')

    ]
