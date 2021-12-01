from django.urls import path

from .import views

urlpatterns = [
    path('helloworld/', views.helloworld),
    path('', views.tasksList, name='task-list'), # as aspas vazias sao para chamar a pagina home do projeto.
    path('yourname/<str:name>', views.yourName, name='your-name'), # posso passar um paramentro para ser impresso na tamplate.
    
]