from django.db import models

class Sensor(models.Model):
    pin = models.IntegerField()
    estado = models.BooleanField()
    def __str__(self):
        return 'pin: '+ str(self.pin)

class Habitacion(models.Model):
    numero = models.IntegerField()
    ocupada = models.BooleanField()
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    def __str__(self):
        return 'Número: '+ str(self.numero)

class Registro(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    horaEntrada = models.TimeField(auto_now_add=True)
    horaSalida = models.TimeField(auto_now=False,blank=True,null=True)
    def __str__(self):
        return 'hora entrada: '+ str(self.horaEntrada) + ' hora salida: '+ str(self.horaSalida)
