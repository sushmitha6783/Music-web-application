from django.contrib import admin
from django.urls import path
from database import views
app_name = 'songs'
urlpatterns = [
    path('', views.home, name='home'),
    path('playlist', views.playlist, name='playlist')
]
