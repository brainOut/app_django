from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required
def home(request):
    return render(request, "home.html")


def log_in(request):
    # si l'utilisateur est déjà loggé: redirection sur la home
    if request.user.is_authenticated:
        return redirect('/app/', permanent=False)
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # mettre l'utilisateur en session: redirection sur la home
            login(request, user)
            return redirect('/app/', permanent=False)
    return render(request, "login.html")


def log_out(request, *args, **kwargs):
    logout(request)
    return redirect('/app/', permanent=False)
