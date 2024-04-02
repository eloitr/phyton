from django.db import models

class Clientes(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50, verbose_name="La dirección")
    email=models.EmailField()
    telefono=models.CharField("Tfno", max_length=7, blank=True, null=True)
    def __str__(self) -> str:
        return self.email

class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=50)
    precio=models.IntegerField()
    
    
    def __str__(self) -> str:
        return self.nombre
    
class Pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()

