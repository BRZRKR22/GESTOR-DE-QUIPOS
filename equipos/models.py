from django.db import models

from django.db import models

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    memoria_ram = models.CharField(max_length=100)
    almacenamiento = models.CharField(max_length=100)
    monitor = models.CharField(max_length=100)
    raton = models.CharField(max_length=100)
    sistema_operativo = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
