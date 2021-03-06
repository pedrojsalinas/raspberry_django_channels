from channels import Group
from django.core.management import BaseCommand
import time
import RPi.GPIO as GPIO
from sensorWorker.models import *

ledPin = 18
button = 26
DOOR_SENSOR_PIN = 5
DOOR_SENSOR_PIN2 = 25

sensores = [DOOR_SENSOR_PIN,DOOR_SENSOR_PIN2]

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(DOOR_SENSOR_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(DOOR_SENSOR_PIN2, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.output(ledPin, GPIO.LOW)

def verificarSensores():
    for i in sensores:
        sensor = Sensor.objects.get(pin=i)
        habitacion = Habitacion.objects.get(sensor_id=sensor.id)
        if (not GPIO.input(i)):
            print("Sensor {} encendido".format(i))
            habitacion.ocupada = True
        else:
            print("Sensor {} apagado".format(i))
            habitacion.ocupada = False
        habitacion.save()


verificarSensores()

def destroy():
        GPIO.output(ledPin, GPIO.LOW)
        GPIO.cleanup()

def my_callback(channel):
    if (not GPIO.input(DOOR_SENSOR_PIN)):
        habitacion = Habitacion.objects.get(pk=1)
        print("led on")
        Group("sensor").send({'text': "1"})
        registro = Registro.objects.create(sensor_id=1)
        habitacion.ocupada = True
        registro.save()
        habitacion.save()

    elif (not GPIO.input(DOOR_SENSOR_PIN2)):
        habitacion = Habitacion.objects.get(pk=2)
        print("led on 1")
        Group("sensor").send({'text': "2"})
        registro = Registro.objects.create(sensor_id=2)
        habitacion.ocupada = True
        registro.save()
        habitacion.save()

    else:
        # registro = Registro.objects.latest('id')
        # registro.horaSalida = time.strftime('%H:%M:%S')
        # habitacion.ocupada = False
        # time.strftime('%H:%M:%S')
        print("led off")
        Group("sensor").send({'text': "Habitacion Libre"})

class Command(BaseCommand):
    help = "Reading sensor on port 26"

    def handle(self, *args, **kwargs):
        GPIO.add_event_detect(DOOR_SENSOR_PIN, GPIO.BOTH, callback=my_callback)
        GPIO.add_event_detect(DOOR_SENSOR_PIN2, GPIO.BOTH, callback=my_callback)
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
