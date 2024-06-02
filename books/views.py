from django.shortcuts import render
from django.http import HttpResponse 

def books(request):
    return HttpResponse("Hi, this is library management site")

def login(request):
    return render(request, "login.html", context = {'page':'Login'})
def student_details(request):
    return render(request, "student_details.html", context = {'page':'student_details'})
def register(request):

    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        password = request.POST.get('password')
        data = request.POST.get('data')
        print(data)


# Create your views here.
