from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'app/home.html')
# Create your views here.

def resource(request):
    return render(request, 'app/resource.html')

def profile(request):
    return render(request, 'app/profile.html')
