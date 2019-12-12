from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import auth, messages


# import in the login_required annonation
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, "accounts/index.html")

"""
logout function
"""
def logout(request):
    auth.logout(request)
    messages.success(request, "Logged out successfully !")
    return redirect(index)
    
"""
This is login function
"""
def login(request):
    return render(request, "accounts/login.html")