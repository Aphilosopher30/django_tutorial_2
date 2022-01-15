from django.shortcuts import render
from django.httpResponse import HttpResponse


# Create your views here.

def index(response):
    return HttpResponse("test")
