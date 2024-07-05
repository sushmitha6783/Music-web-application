from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request , 'signup.html')


def loginpage(request):
    return render(request , 'loginpage.html')

def index(request):
    return render(request , 'index.html')

def playlist(request):
    return render(request , 'playlist.html')

def about(request):
    return render(request , 'about.html')


