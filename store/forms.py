from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.forms import fields, widgets

class RegistrationForm(UserCreationForm):
    password1=forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}))
    password2=forms.CharField(label='confirm password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'confirm password'}))
    email=forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email Address'}))

    class Meta:
        model=User
        fields={'username','email','password1','password2'}
        labels={'email':'Email'}
        widgets={'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Username'})}
        
class LoginForm(AuthenticationForm):
        username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
        password=forms.CharField(label=("password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

    
