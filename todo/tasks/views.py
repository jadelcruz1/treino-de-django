from django.shortcuts import render
from django.http import HttpResponse, request

def helloworld(request):
    return HttpResponse('teste aplicação')

def tasksList(request):
    return render(request, 'tasks/list.html') #para criar uma view sempre terá de ter o request e o return.

def yourName(request, name):
    return render (request, 'tasks/yourname.html', {'name': name})

