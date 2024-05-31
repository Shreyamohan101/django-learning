from django.shortcuts import render
from django.http import HttpResponse 

def books(request):
    return HttpResponse("Hi, this is library management site")

def withoutlogin(request):
    return render(request, "withoutlogin.html", context = {'page':'withoutLogin'})
def register(request):
    return render(request, "register.html", context = {'page':'register'})


# Create your views here.
