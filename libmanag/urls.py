"""
URL configuration for libmanag project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin          #//import here first
from django.urls import path
from books.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('book/', book , name = "book"),
    path('Details/', student_details , name = "student_details"),
    path('Details/', student_details , name = "student_details"),
    path('book_detail/', book_detail, name = "book_detail"),
    path('', login, name='login'),
     path('register/', register, name='register'),
]
