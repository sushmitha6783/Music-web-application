from django.shortcuts import render

# Create your views here.


def home(request):
    # return HttpResponse("This is HTML Website")
    return render(request , 'loginpage.html')