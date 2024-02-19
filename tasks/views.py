from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
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
                return HttpResponse("Usuario creado")
            except:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Username already existe'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Password do not match'
        })
        # print(request.POST) Esto envia los datos del formulario, super importante
