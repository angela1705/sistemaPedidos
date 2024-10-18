from django.db import models

# Create your models here.
from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    ESTADO_CHOICES = [
        ('espera', 'En espera'),
        ('preparacion', 'En preparación'),
        ('listo', 'Listo para entregar'),
    ]
    
    nombre_cliente = models.CharField(max_length=100)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    para_llevar = models.BooleanField(default=False)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='espera')
    observaciones = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.producto.nombre} - {self.nombre_cliente} - {self.estado}"
