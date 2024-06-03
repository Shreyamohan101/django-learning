from django.shortcuts import render, redirect , get_object_or_404
from django.http import HttpResponse 
from .models import*

def books(request):
    return HttpResponse("Hi, this is library management site")

def login(request):
    return render(request, "login.html", context = {'page':'Login'})
def student_details(request):
    return render(request, "student_details.html", context = {'page':'student_details'})

def register(request):
    if request.method == 'POST':
        data = request.POST
        firstname = data.get('firstname')
        lastname =  data.get('lastname')
        username =  data.get('username')
        password =  data.get('password')
        print(firstname)
        print(lastname)
        print(username)
        print(password)
        register.object.create(
            firstname = firstname,
            lastname = lastname,
            username = username,
            password = password,
        )

        Member.objects.create(name=f"{firstname} {lastname}", username=username, password=password)
        
        return redirect('thank_you')
    return render(request, 'register.html', context={'page': 'Register'})
    #     return redirect ('/register/')

    #     return HttpResponse("Registration successful")
    # else:
    #     return render(request, "register.html", context={'page': 'Register'})

# Create your views here.

def login(request):
    if request.method == 'POST':
        # Accessing form data using request.POST
        Username = request.POST.get('Username')
        password = request.POST.get('password')
        
        # You can now use the form data (e.g., authenticate the user)
        if Username == 'admin' and password == 'secret':  # Example authentication
            return HttpResponse("Welcome, admin!")
        else:
            return HttpResponse("Invalid credentials")

    return render(request, 'login.html')

# views.py

def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        isbn = request.POST.get('isbn')
        category = request.POST.get('category')

        Book.objects.create(
            title=title,
            author=author,
            isbn=isbn,
            category=category,
        )
        return redirect('/book_list/')

    return render(request, 'add_book.html')

    #  return redirect ('/student_details/')
      
    # return render(request, 'student.html', context={'page': 'Details'})


    

# Detail view to display a single book
def book_list(request):
      books = Book.objects.all()
      return render(request, 'books/book_list.html', {'books': books})
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})

# View to add a new book

