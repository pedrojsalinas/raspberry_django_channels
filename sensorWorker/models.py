from django.db import models

# Create your models here.
class Boton(models.Model):
    pin = models.IntegerField()
    def __str__(self):
        return 'pin: '+ str(self.pin)

class Registro(models.Model):
    boton = models.ForeignKey(Boton, on_delete=models.CASCADE)
    hora = models.TimeField(auto_now=True)
    def __str__(self):
        return 'hora: '+ str(self.hora)
