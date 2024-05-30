from django.shortcuts import render
from django.http import HttpResponse 

def books(request):
    return HttpResponse("Hi, this is library management site")


# Create your views here.
