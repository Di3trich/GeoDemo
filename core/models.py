from django.db import models


class Cliente(models.Model):
    nombres = models.CharField(max_length=128)
    apellidos = models.CharField(max_length=128)
    documento = models.IntegerField()

    def save(self, *args, **kwargs):
        self.nombres = self.nombres.upper()
        self.apellidos = self.apellidos.upper()
        super(Cliente, self).save(*args, **kwargs)

    @property
    def direccion_principal(self):
        return self.direcciones.filter(principal=True).first()

    def __str__(self):
        return "%s, %s - (%s)" % (self.apellidos, self.nombres, self.direccion_principal)


class Direccion(models.Model):
    direccion = models.CharField(max_length=256)
    principal = models.BooleanField()
    latitud = models.DecimalField(max_digits=11, decimal_places=9, null=True, blank=True)
    longitud = models.DecimalField(max_digits=11, decimal_places=9, null=True, blank=True)
    cliente = models.ForeignKey(Cliente, related_name='direcciones')

    def save(self, *args, **kwargs):
        if self.cliente.direcciones.count() == 0:
            self.principal = True
        elif self.principal:
            self.cliente.direcciones.update(principal=False)
        super(Direccion, self).save(*args, **kwargs)

    def __str__(self):
        return "%s (%s)" % (self.direccion, self.principal)


class Imagen(models.Model):
    descripcion = models.CharField(max_length=128)
    imagen = models.ImageField(upload_to='images', max_length=256)
    direccion = models.ForeignKey(Direccion, related_name='imagenes')

    def __str__(self):
        return self.descripcion;
