from django.contrib import admin
from django.urls import include, path
from database import views

app_name = 'playlists'
urlpatterns = [
        path('', views.home, name='home')
    ]
