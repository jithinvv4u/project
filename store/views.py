from .forms import *
from django.shortcuts import render

# Create your views here.
def Home(req):
    return render(req,'store/index.html')

def RegistrationView(req):
    context={}
    context['form']=RegistrationForm()
    if req.method=='GET':
        return render(req,'store/register.html',context)

def loginView(req):
    context={}
    context['form']=LoginForm()
    if req.method=='GET':
        return render(req,'store/login.html',context)
        