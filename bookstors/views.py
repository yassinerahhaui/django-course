from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('<h1>home page</h1>')

def users(request):
    return HttpResponse('<h1>users page</h1>')

def about(request):
    return HttpResponse('<h1>about page</h1>')