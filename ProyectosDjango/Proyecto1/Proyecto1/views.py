import datetime

from django.http import HttpResponse
from django.template import Template, Context
import random

class Persona(object):
    def __init__(self, nombre, apellido):
        
        self.nombre = nombre
        self.apellido=apellido
    
        

def saludo(request): #primera vista
    p1=Persona("Eloi", "Traver")
    numero = random.randrange(100)
    #nombre = "Eloi"
    #apellido = "Traver"
    ahora = datetime.datetime.now()
    doc_externo = open("C:/Users/eloit/phyton/ProyectosDjango/Proyecto1/Proyecto1/plantillas/mi_plantilla.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora, "numero_aleatorio":numero})
    
    documento = plt.render(ctx)
    
    return HttpResponse(documento)


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


