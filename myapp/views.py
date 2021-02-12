from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "myapp/index.html")

def page1(request):
    return render(request, "myapp/page1.html")

def page2(request):
    return render(request, "myapp/page2.html")

def page3(request):
    return render(request, "myapp/page3.html")
