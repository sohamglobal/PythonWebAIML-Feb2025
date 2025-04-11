from django.shortcuts import render

def homepage(request):
    return render(request,"index.html")

def about(request):
    return render(request,"aboutus.html")

def welcome(request):
    
    if request.method=="POST":
        nm=request.POST.get("name")
        print(nm)
    return render(request,"welcomeuser.html",{"user":nm})