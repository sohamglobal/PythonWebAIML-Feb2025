from django.shortcuts import render, redirect


def homepage(request):
    return render(request,"index.html")

def userlogin(request):
    if request.method == "POST":
        unm = request.POST.get("username")
        ups = request.POST.get("password")
        if unm == "sharayu" and ups == "spider":
            request.session["is_logged_in"]=True
            request.session["username"] = unm
            return redirect("dashboard")
        else:
            return render(request,"loginfailed.html",{"error":"Invalid credentials"})
    #return render(request,"userlogin.html")

def dashboard(request):
    if not request.session.get("is_logged_in"):
        return redirect("homepage")
    
    nm=request.session.get("username")
    return render(request,"dashboard.html",{"user":nm})