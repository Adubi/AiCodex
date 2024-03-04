from django.shortcuts import render, HttpResponse
from .models import MyModel


def home(request):  
    print(request.user)
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')