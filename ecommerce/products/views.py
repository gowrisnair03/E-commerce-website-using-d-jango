from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Products Home")

def create_product():
    return HttpResponse("Products Home")
