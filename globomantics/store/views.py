from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello")

def detail(request):
    return HttpResponse("Hello details")

def electronics(request):
    return HttpResponse("Electronics")