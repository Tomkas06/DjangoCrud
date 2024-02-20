from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TaskForm
from .models import Task
# Create your views here.

#Esto crea una "pagina" con contenido hello world

#Para pasar datos del backend al frontend se crea una variable en la funcion:
"""
def funcion(request):
    variable = ...
    return render(request, 'index.html', {
        "show": variable
    }
"""
#Y dentro del HTML, se pone en entre doble llave, {{}}, la variable, que seria show


def home(request):
    return render(request, 'home.html')
      
def tasks(request):
    tasks = Task.objects.filter(user=request.user)
    
    return render(request, 'tasks.html', {
        'tasks': tasks
    })

def create_task(request):
   if request.method == 'GET':
        return render(request, 'create_task.html', {
            'form': TaskForm
        })    
   else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'create_task.html', {
                'form': TaskForm,
                'error': 'Pruebe datos validos'
            })

def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Username is incorrect'
            })
        else:
            login(request, user)
            return redirect('tasks')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm,

        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'User already exists'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Password do not match'
        })
        # print(request.POST) Esto envia los datos del formulario, super importante