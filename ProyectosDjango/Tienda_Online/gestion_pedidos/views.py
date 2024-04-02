from django.shortcuts import render
from django.http import HttpResponse
from gestion_pedidos.models import Articulos

def busqueda_productos(request):
    return render(request, "busqueda_productos.html")

def buscar(request):  
    producto=request.GET["producto"]
    if request.GET["producto"]:
        mensaje="Artículo buscado: %s"%producto
        articulos=Articulos.objects.filter(nombre__icontains=producto)
        if articulos:
            art=len(articulos)
            articulos_view=articulos
            return render(request, "resultados_busqueda.html", {"articulos":art, "query":producto, "articulos_view":articulos_view})
        else:
            art=0
            return render(request, "resultados_busqueda.html", {"articulos":art, "query":producto})
    else:
        mensaje="No has introducido nada"    
    return HttpResponse(mensaje)