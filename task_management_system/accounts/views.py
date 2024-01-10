from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from tasks.models import Tasks
from tasks.helpers import *
from .forms import CreateUserForm
from tasks.forms import *
from django.contrib.auth.decorators import login_required


def registerPage(request):
    if request.user.is_authenticated:
        return redirect("home")
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
        return render(request, "accounts/register.html", context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect("home")
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
        return render(request, "accounts/login.html", context)


def logoutUser(request):
    logout(request)
    return redirect("login")


@login_required(login_url="login")
def homePage(request):
    user_tasks = get_user_tasks(request)
    _tasks_assigned_to_user = tasks_assigned_to_user(request)
    _tasks_assigned_by_current_user = tasks_assigned_by_current_user(request)
    task_assignment_form = TaskAssignmentForm()
    context = {
        "user_tasks": user_tasks,
        "usernames": get_users(request),
        "task_assignment_form":task_assignment_form,
        "tasks_assigned_to_user": _tasks_assigned_to_user,
        "tasks_assigned_by_current_user": _tasks_assigned_by_current_user,
    }
    return render(request, "accounts/home.html", context)


@login_required(login_url="login")
def get_users(request):
    usernames = User.objects.values("id", "username")
    return usernames
