from django.shortcuts import render
from django.core.context_processors import csrf

# Create your views here.
def loginview(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'NLP/login.html', c)
