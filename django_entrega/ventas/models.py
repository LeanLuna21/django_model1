from django.db import models
from stock.models import Producto

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    mail = models.EmailField()
    dni = models.IntegerField()

class Transaccion(models.Model):
    nro_transaccion = models.IntegerField() 
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE,related_name='ventas')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_total = models.FloatField() 
    fecha_de_venta = models.DateField()
