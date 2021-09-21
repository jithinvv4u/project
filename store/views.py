from django.http.response import HttpResponse
from .forms import *
from django.shortcuts import render
from django.contrib import messages
# Create your views here.
def Home(req):
    return render(req,'store/index.html')

def RegistrationView(req):
    context={}
    context['form']=RegistrationForm()
    if req.method=='GET':
        return render(req,'store/register.html',context)
    elif req.method=='POST':
        form=RegistrationForm(req.POST)
        if form.is_valid():
            messages.success(req,"congratulation! Registration Successfull")
            form.save()
        else:
            return HttpResponse("not valid")
        return render(req,'store/login.html')


def loginView(req):
    context={}
    context['form']=LoginForm()
    if req.method=='GET':
        return render(req,'store/login.html',context)
        