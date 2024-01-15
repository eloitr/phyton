from django.http import HttpResponse

def saludo(request): #primera vista
    
    return HttpResponse("Hola, esta es mi primera pagina conn django! Accede al contenido: http://localhost:8000/contenido/")

def despedida(request):
    
    return  HttpResponse("Adioooooooos chicos")  

def contenido(request):
    
    return HttpResponse("Este es el contenido")     

