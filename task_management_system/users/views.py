from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:            
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get("username")
                messages.success(request, "Account was created for " + user)
                return redirect("login")
            else:
                print(f"{form.errors}")

        context = {"form": form}
        return render(request, "users/register.html", context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:  
        context = {}
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect("home")
            else:
                messages.info(request, "Username or password is incorrect")
        return render(request, "users/login.html", context)


def logoutUser(request):
    logout(request)
    return redirect("login")


@login_required(login_url="login")
def homePage(request):
    context = {}
    return render(request, "users/home.html", context)
