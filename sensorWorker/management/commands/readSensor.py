from channels import Group
from django.core.management import BaseCommand
import time
import RPi.GPIO as GPIO
from sensorWorker.models import Registro

ledPin = 18
button = 26
DOOR_SENSOR_PIN = 5


GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(DOOR_SENSOR_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.output(ledPin, GPIO.LOW)

def destroy():
        GPIO.output(ledPin, GPIO.LOW)
        GPIO.cleanup()

def my_callback(channel):
    if (not GPIO.input(DOOR_SENSOR_PIN)):
        GPIO.output(ledPin, GPIO.HIGH)
        print("led on")
        Group("sensor").send({'text': "Habitacion Ocupada"})
        registro = Registro.objects.create(boton_id=2)
        registro.save()
    else:
        GPIO.output(ledPin, GPIO.LOW)
        print("led off")
        Group("sensor").send({'text': "Habitacion Libre"})

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
