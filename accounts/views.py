from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import auth, messages
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required

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

@login_required
def profile(request):
    return HttpResponse("Profile")
    
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # check if the username and password matches
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                # actually log the user in
                auth.login(user=user, request=request)
                messages.success(request, "You have registered successfully")
            else:
                messages.error(request, "Registration failed")
            return redirect(reverse('index'))
        else:
            return render(request, "accounts/register.html",{
                'form': form
            })
    else:
        register_form = UserRegistrationForm()
        return render(request, "accounts/register.html", {
            'form': register_form
        })