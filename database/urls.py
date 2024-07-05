from django.contrib import admin
from django.urls import include, path
from database import views
app_name = 'database'

urlpatterns = [
        path('', views.home, name='home'),
        path('loginpage', views.loginpage, name='loginpage'),
        path('index', views.index, name='index'),
        path('playlist', views.playlist, name='playlist'),
        path('about', views.about, name='about'),

    ]
