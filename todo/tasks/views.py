from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, request

from .models import Task


    
    
def helloworld(request):
    return HttpResponse('teste aplicação')

def tasksList(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/list.html', {'tasks':tasks}
) #para criar uma view sempre terá de ter o request e o return.

def yourName(request, name):
    return render (request, 'tasks/yourname.html', {'name': name})

def taskView(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task': task})