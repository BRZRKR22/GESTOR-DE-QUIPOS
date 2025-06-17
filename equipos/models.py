from django.db import models

ESTADO_CHOICES = [
    ('disponible', 'Disponible'),
    ('mantenimiento', 'En mantenimiento'),
    ('no_disponible', 'No disponible'),
]

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    memoria_ram = models.CharField(max_length=50)
    almacenamiento = models.CharField(max_length=50)
    monitor = models.CharField(max_length=100)
    raton = models.CharField(max_length=100)
    sistema_operativo = models.CharField(max_length=100)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='disponible')

    def __str__(self):
        return self.nombre
