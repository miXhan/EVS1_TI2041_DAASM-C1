from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def vistaUno(request):
    html=""""
    <h1>Estas son pruebas</h1>
    <h1>Estos son ejemplos</h1>
    <h1>Esto es un destre</h1>
    <h2>Hola mundo</h2>
    
    """
    return HttpResponse (html)

# Create your views here.
