from django.http.response import HttpResponse
from django.shortcuts import render

def cadastro(request):
    return render(request, 'index.html')
    # return HttpResponse('cadastro')

def logar(request):
    return render(request, 'login.html')
