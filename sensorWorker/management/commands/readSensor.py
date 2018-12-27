from channels import Group
from django.core.management import BaseCommand
import time
import RPi.GPIO as GPIO

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(26, GPIO.IN)
# GPIO.setup(18, GPIO.OUT)

ledPin = 18
button = 26

GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by physical location
GPIO.setup(ledPin, GPIO.OUT)   # Set ledPin's mode is output
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(ledPin, GPIO.LOW) # Set ledPin low to off led

def destroy():
        GPIO.output(ledPin, GPIO.LOW)     # led off
        GPIO.cleanup()                     # Release resource

def my_callback(channel):
    if (not GPIO.input(button)):     # if port 25 == 1
        # print("Rising edge detected on 26")
        GPIO.output(ledPin, GPIO.HIGH)
        print("led on")
        Group("sensor").send({'text': "Button pushed"})
    else:                  # if port 256!= 1
        # print("Falling edge detected on 26")
        GPIO.output(ledPin, GPIO.LOW)
        print("led off")
        Group("sensor").send({'text': "Button released"})

class Command(BaseCommand):
    help = "Reading sensor on port 26"

    def handle(self, *args, **kwargs):
        GPIO.add_event_detect(26, GPIO.BOTH, callback=my_callback)
        try:
                while True:
                    input("Press Enter when ready\n>")
                    destroy()
        except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
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
