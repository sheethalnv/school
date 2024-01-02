from django.contrib import messages,auth
from django.http import HttpResponseRedirect, request
from django.shortcuts import render, redirect
from django.urls import reverse

from schoolapp.models import Department, Details, Course, Purpose


# Create your views here.
def home(request):
    return render(request,'home.html')
def login(request):

    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request,"utility.html")
        else:
            messages.info(request, "invalid credentials")
            return redirect("login")
    return render(request, "login.html")

def register(request):
    if request.method=="POST":
        uname=request.POST['uname']
        password = request.POST['password']
        cpassword=request.POST['cpassword']
        from django.contrib.auth.models import User
        if password==cpassword:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"username exists")
                return redirect('register')

            else:
                user=User.objects.create_user(username=uname,password=password)
                user.save();
                return redirect('school:login')
        else:
            print("passwords did not matches")
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')

def utility(request):
    department=Department.objects.all()
    purpose=Purpose.objects.all()
    if request.method == "POST":
        print('success')
        name = request.POST['name']
        dob = request.POST['dob']
        gender = request.POST['gender']
        phone = request.POST['phnumber']
        email = request.POST['email']
        address = request.POST['address']
        department = request.POST['department']
        course = request.POST['course']
        purpose = request.POST['purpose']
        details=Details(name=name,dob=dob,gender=gender,phone=phone,address=address,email=email,
                        department=department,course=course,purpose=purpose)

        details.save()
        return redirect('/')
    return render(request,'form.html',{'department':department,'purpose':purpose})

def details(request):

    if request.method == "POST":
        print('success')
        name = request.POST['name']
        dob = request.POST['dob']
        gender = request.POST['gender']
        phone = request.POST['phnumber']
        email = request.POST['email']
        address = request.POST['address']
        department = request.POST['department']
        course = request.POST['course']
        purpose = request.POST['purpose']
        details=Details(name=name,dob=dob,gender=gender,phone=phone,address=address,email=email,
                        department=department,course=course,purpose=purpose)

        details.save()
        return redirect('/')

    return render(request,'form.html')



def load_cources(request):
    department = request.GET.get ('department')
    courses = Course.objects.filter(department=department)
    return render(request,'dropdown.html',{'courses':courses})