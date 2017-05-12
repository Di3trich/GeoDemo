from django.db import models


class Cliente(models.Model):
    nombres = models.CharField(max_length=128)
    apellidos = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        self.nombres = self.nombres.upper()
        self.apellidos = self.apellidos.upper()
        super(Cliente, self).save(*args, **kwargs)


class Direccion(models.Model):
    direccion = models.CharField(max_length=256)
    principal = models.BooleanField()
    cliente = models.ForeignKey(Cliente, related_name='direcciones')

    def save(self, *args, **kwargs):
        if self.principal:
            self.cliente.direcciones.update(principal=False)
        super(Direccion, self).save(*args, **kwargs)
