from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import auth, messages
from .forms import UserLoginForm

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
    if request.method == "POST":
        # populate login form with the user's input
        login_form = UserLoginForm(request.POST)
        
        # check validity of login form
        if login_form.is_valid():
            # use auth.authenticate to check if username and password is correct
           
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            #if user details are correct
            if user:
                auth.login(user=user, request=request)
                return redirect(reverse('index'))
        
    else:
        form = UserLoginForm()
        return render(request, 'accounts/login.html', {
            'form':form
        })