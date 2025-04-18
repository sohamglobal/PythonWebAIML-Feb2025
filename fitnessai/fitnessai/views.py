from django.shortcuts import render,redirect
from .services import FitnessServices

def index(request):
    return render(request,"index.html")

def login(request):
    if request.method=="POST":
        uid=request.POST.get("userid")
        psw=request.POST.get("password")
        if uid=="sharayu" and psw=="spider":
            request.session["authenticated"]=True
            request.session["userid"]=uid
            return redirect("dashboard")
        else:
            return render(request,"loginfailed.html")

def dashboard(request):
    if not request.session.get("authenticated"):
        return redirect("index")   

    uid=request.session.get("userid")
    return render(request,"dashboard.html",{"user":uid}) 

def addprofile(request):
    return render(request,"newprofile.html")

def storeprofile(request):
    if request.method=="POST":
        name=request.POST.get("person_name")
        age=int(request.POST.get("age"))
        gender=request.POST.get("gender")
        height=float(request.POST.get("height_cm"))
        weight=int(request.POST.get("weight_kg"))
        bmi=float(request.POST.get("bmi"))
        food=request.POST.get("food_type")
        steps=int(request.POST.get("steps_per_day"))
        fs=FitnessServices()
        result=fs.addnewprofile(name,age,gender,height,weight,bmi,food,steps)
        if result:
            return render(request,"profileadded.html")
        else:
            return render(request,"profileaddfailed.html")
