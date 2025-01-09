from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.
def login_view(request):
    username = "waseem2" # request.POST["username"]
    password = "264c8aea" #request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        print("Login Here!")
        return redirect("/")
        # Redirect to a success page.
    return render(request, "auth/login.html", {})


# def register_view(request):
#     return render(request,"auth/login.html")