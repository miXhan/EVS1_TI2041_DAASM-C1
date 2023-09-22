from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def vistaUno(request):
    html=""""
    <h1>Hola mundo</h1>
    <h1>piedad profesor</h1>
    <h1>porque no me funciona</h1>
    <h1>raios</h1>
   
    """
    return HttpResponse (html)
  


    