
from django.shortcuts import render,redirect
from django.http import HttpResponse 
from .models import Employee

#create your views here.

#def index(request):
    #return render(request,"index.html",{})

def home(request):
    return render(request,"home.html",{})


def register(request):
    if request.method=='POST':
        ename=request.POST.get("name")
        efathername=request.POST.get("fathername")
        emothername=request.POST.get("mothername")
        ecourse=request.POST.get("course")
        egender=request.POST.get("gender")
        edateonbirth=request.POST.get("dateonbirth")
        ebloodgroup=request.POST.get("bloodgroup")
        ephoneno=request.POST.get("phoneno")
        eaddress=request.POST.get("address")
        email=request.POST.get("email")
        epassword=request.POST.get("password")
        e=Employee()
        e.name=ename
        e.fathername=efathername
        e.mothername=emothername
        e.course=ecourse
        e.gender=egender
        e.dateonbirth=edateonbirth
        e.bloodgroup=ebloodgroup
        e.phoneno=ephoneno
        e.address=eaddress
        e.email=email
        e.password=epassword
        e.save()
    return render(request,"register.html",{})

def view(request):
    e=Employee.objects.all()
    return render(request,"view.html",{'emp':e})

def update(request,id):
    s=Employee.objects.get(pk=id)
    return render(request,"update.html",{'std':s})

def upemp(request):
    ename=request.POST.get("name")
    efathername=request.POST.get("fathername")
    emothername=request.POST.get("mothername")
    ecourse=request.POST.get("course")
    egender=request.POST.get("gender")
    edateonbirth=request.POST.get("dateonbirth")
    ebloodgroup=request.POST.get("bloodgroup")
    ephoneno=request.POST.get("phoneno")
    eaddress=request.POST.get("address")
    email=request.POST.get("email")
    epassword=request.POST.get("password")
        
    e=Employee.objects.get(pk=id)
    e.name=ename
    e.fathername=efathername
    e.mothername=emothername
    e.course=ecourse
    e.gender=egender
    e.dateonbirth=edateonbirth
    e.bloodgroup=ebloodgroup
    e.phoneno=ephoneno
    e.address=eaddress
    e.email=email
    e.password=epassword
    e.save()
    return redirect('home')

def delemp(request,id):
     s=Employee.objects.get(pk=id)
     s.delete()
     return redirect('home')