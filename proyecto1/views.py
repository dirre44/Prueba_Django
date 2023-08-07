from django.http import HttpResponse
from django.template import Template, Context
import datetime

def saludar (request):
    return HttpResponse("Hola mundo!")

def despidiendo (request):
    return HttpResponse("<h1>Chau mundo!</h1>")

def saludo_al_nombre (request, nombre):
    return HttpResponse(f"<h1>Hola {nombre}</h1>")

def calcula_nacimiento (request, edad):
    anio_actual = datetime.datetime.today().year
    anio_de_nacimiento = anio_actual-int(edad)
    mensaje = f"usted nacio en el año {anio_de_nacimiento}"
    return HttpResponse(mensaje)

def probandohtml (request): 

    diccionario = {}
    archivo = open (r"E:\salvado\Coderhouse\Clase 17 - django\proyecto1\plantillas\template1.html")
    contenido = archivo.read()
    archivo.close()
    plantilla = Template(contenido)
    contexto = Context(diccionario)
    documento = plantilla.render(contexto)
    return HttpResponse(documento)
