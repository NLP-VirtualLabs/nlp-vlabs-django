from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.template import RequestContext
from NLP.forms import *

def main_page(request):
    return render(request,'NLP/main_page.html',{'user':request.user})

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

def register_user(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)     # create form object
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form':form})
