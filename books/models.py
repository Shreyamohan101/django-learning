from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    rollno = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    Book_issued = models.CharField(max_length=100)
    Date_issued = models.DateField()
    Date_return = models.DateField(null = True)