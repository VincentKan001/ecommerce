from django import forms

class UserLoginForm(forms.Form):
    """this is a log in form"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)