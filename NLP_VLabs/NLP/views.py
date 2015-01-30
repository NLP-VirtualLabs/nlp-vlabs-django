from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.template import RequestContext
from NLP.forms import *

def main_page(request):
    return render(request,'NLP/main_page.html',{'user':request.user})

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/login')

def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
        )
        return HttpResponseRedirect('/login')
    else:
        form = RegistrationForm()

    return render(request,'registration/register.html',{'form':form})

