from django.db import models

# Create your models here.
class Purpose(models.Model):
    name=models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.name
class Department(models.Model):
    name=models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.name

class Course(models.Model):
    name=models.CharField(max_length=100,unique=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Details(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField()
    gender=models.CharField(max_length=10)
    phone=models.CharField(max_length=12)
    email=models.CharField(max_length=20)
    address=models.CharField(max_length=200)
    department=models.CharField(max_length=20)
    course=models.CharField(max_length=20)
    purpose=models.CharField(max_length=200)
    def __str__(self):
        return self.name

