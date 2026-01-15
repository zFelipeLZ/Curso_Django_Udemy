from django.shortcuts import render
from django.http import HttpResponse

# HTTP REQUEST
def home(request):
    return render(request, 'home.html')
    # return HTTP Response

# HTTP REQUEST
def contato(request):
    return HttpResponse('Contato')
    # return HTTP Response

# HTTP REQUEST
def sobre(request):
    return HttpResponse('Sobre')
    # return HTTP Response