import datetime

from django.http import HttpResponse
#from django.template import Template, Context --> haciendo sin importar el dir a settings, ver curso pílsoras 1-8
import random
#from django.template.loader import get_template --> para utilizar la simplificació del vídeo 8
from django.shortcuts import render
class Persona():#object
    def __init__(self, nombre, apellido):
        
        self.nombre = nombre
        self.apellido = apellido
    
        

def saludo(request): #primera vista
    p1=Persona("Terròs", "Traver")
    numero = random.randrange(100)
    #nombre = "Eloi"
    #apellido = "Traver"
    temas_del_curso = ["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue de la aplicación"]#"Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue de la aplicación"
    ahora = datetime.datetime.now()

    return render(request, 'mi_plantilla.html', {
                "nombre_persona":p1.nombre, 
                "apellido_persona":p1.apellido,
                "momento_actual":ahora,
                "numero_aleatorio":numero,
                "temas":temas_del_curso})

def f1(request):
    ahora = datetime.datetime.now()

    return render(request, 'f1.html', {"momento_actual":ahora})

def troll(request):
    ahora = datetime.datetime.now()

    return render(request, 'troll.html', {"momento_actual":ahora})









def despedida(request):
    
    return  HttpResponse("Adioooooooos chicos")  


def contenido(request):
    
    return HttpResponse("Este es el contenido")     


def dame_hora(request):
    
    hora_actual = datetime.datetime.now()
    respuesta = f"<html><body><h2>Hora actual: {hora_actual} </h2></body></html>"
    return HttpResponse(respuesta)


def calculaEdad(request, edad, agno):
    
    #edad_actual = 15
    periodo = agno - 2024
    edad_futura = periodo + edad
    documento = f"<html><body><h2>Con {edad} años, en el año {agno} tendras {edad_futura} años. </h2></body></html>"
    return HttpResponse(documento)


