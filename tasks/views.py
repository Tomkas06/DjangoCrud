from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

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

def helloworld(request):
    return render(request, 'signup.html', {
        'form': UserCreationForm
    })