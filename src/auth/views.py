from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your views here.
def login_view(request):
    # print(request.method, request.POST or None) # for print requets method and password on terminal
    if request.method == "POST":
        username = request.POST["username"] or None
        password = request.POST["password"] or None
        # eval("print('hello')")
        if all ([username, password]):
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print("Login Here!")
                return redirect("/")
                # Redirect to a success page.
    return render(request, "auth/login.html", {})


def register_view(request):
    if request.method == "POST":
        print(request.POST)
        username = request.POST["username"] or None
        email = request.POST["email"] or None
        password = request.POST["password"] or None
        
        #Django Forms
        # username_exists = User.objects.filter(username__iexact=username).exists()
        # email_exists = User.objects.filter(email__iexact=email).exists()
        try:
            User.objects.create_user(username=username, email=email, password=password)
        except:
            pass
    return render(request,"auth/register.html")