from channels import Group
from django.core.management import BaseCommand
import time
import RPi.GPIO as GPIO
from sensorWorker.models import *

ledPin = 18
button = 26
DOOR_SENSOR_PIN = 5


GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(DOOR_SENSOR_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.output(ledPin, GPIO.LOW)

def verificarSensores():
    habitacion = Habitacion.objects.get(pk=1)
    if (not GPIO.input(DOOR_SENSOR_PIN)):
        print("Sensor {} encendido".format(DOOR_SENSOR_PIN))
        habitacion.ocupada = True
    else:
        print("Sensor {} apagado".format(DOOR_SENSOR_PIN))
        habitacion.ocupada = False
    habitacion.save()


verificarSensores()

def destroy():
        GPIO.output(ledPin, GPIO.LOW)
        GPIO.cleanup()

def my_callback(channel):
    habitacion = Habitacion.objects.get(pk=1)
    if (not GPIO.input(DOOR_SENSOR_PIN)):
        GPIO.output(ledPin, GPIO.HIGH)
        print("led on")
        Group("sensor").send({'text': "Habitacion Ocupada"})
        registro = Registro.objects.create(sensor_id=1)
        habitacion.ocupada = True

    else:
        GPIO.output(ledPin, GPIO.LOW)
        # registro = Registro.objects.latest('id')
        registro.horaSalida = time.strftime('%H:%M:%S')
        habitacion.ocupada = False
        # time.strftime('%H:%M:%S')
        print("led off")
        Group("sensor").send({'text': "Habitacion Libre"})
    registro.save()
    habitacion.save()

class Command(BaseCommand):
    help = "Reading sensor on port 26"

    def handle(self, *args, **kwargs):
        GPIO.add_event_detect(DOOR_SENSOR_PIN, GPIO.BOTH, callback=my_callback)
        try:
                while True:
                    input("Press Enter when ready\n>")
                    destroy()
        except KeyboardInterrupt:
                destroy()














    # help = "Simulates reading sensor and sending over Channel."

    # def handle(self, *args, **kwargs):
    #     x = 0
    #     while True:
    #         textToSend = "Sensor reading = " + str(x)
    #         Group("sensor").send({'text': textToSend})
    #         time.sleep(2)
    #         x = x + 1
    #         self.stdout.write("Sensor reading...." + str(x))
