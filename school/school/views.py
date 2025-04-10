from django.shortcuts import render

def homepage(request):
    return render(request,"index.html")

def about(request):
    return render(request,"aboutus.html")