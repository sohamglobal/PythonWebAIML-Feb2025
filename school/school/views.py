from django.shortcuts import render
from .services import DataOperations

def homepage(request):
    return render(request,"index.html")

def about(request):
    return render(request,"aboutus.html")

def welcome(request):
    
    if request.method=="POST":
        nm=request.POST.get("usernm")
        print(nm)
    return render(request,"welcomeuser.html",{"user":nm,"developer":"Ethan Hunt"})

def showsquare(request):
    if request.method=="POST":
        n=int(request.POST.get("num"))
        sq=n*n
    return render(request,"showsquare.html",{"number":n,"square":sq})

def searchaccount(request):
    if request.method=="POST":
        no=int(request.POST.get("ano"))
        print(no)
        obj=DataOperations()
        dic=obj.serachaccountnumber(no)
    
    return render(request,"accountinfo.html",dic)