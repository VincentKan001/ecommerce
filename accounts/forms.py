from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

# our own user model
from .models import MyUser

class UserLoginForm(forms.Form):
    """this is a log in form"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    

"""
User registration form
"""
class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password Confirmation", widget=forms.PasswordInput)
    
    def clean_email(self):
        User = get_user_model()
        
        user_provided_email = self.cleaned_data.get('email')
        
        # to see if the email already exist in system
        if User.objects.filter(email=user_provided_email):
            # if email exist, raise an error
            raise forms.ValidationError("This email address is already in use")
        
        return user_provided_email
        
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if not password1 or not password2:
            raise forms.ValidationError("Please provide your password again")
        
        if password1 != password2:
            raise forms.ValidationError("Make sure both passwords are the same")
            
        # return password2 as it passed all validation rules
        return password2
        
    class Meta:
        model = MyUser
        fields = ['email', 'username', 'password1', 'password2']