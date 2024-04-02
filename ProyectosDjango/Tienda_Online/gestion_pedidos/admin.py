from django.contrib import admin
from gestion_pedidos.models import Clientes, Articulos, Pedidos

class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre", "telefono", "email")
    search_fields=("nombre", "telefono", "email")
    list_filter=("nombre", "telefono", "email")

class ArticulosAdmin(admin.ModelAdmin):
    list_display=("nombre", "seccion", "precio")
    search_fields=("nombre", "seccion", "precio")
    list_filter=("nombre", "seccion", "precio")

class PedidosAdmin(admin.ModelAdmin):
    list_display=("numero", "fecha", "entregado")
    search_fields=("numero", "fecha", "entregado")
    list_filter=("numero", "fecha", "entregado")
    date_hierarchy="fecha"
    




admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos, PedidosAdmin)