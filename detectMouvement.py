
# Import des modules
import RPi.GPIO as GPIO
import time

# Initialisation de la numerotation et des E/S
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT,initial = GPIO.LOW)


GPIO.output(37,GPIO.HIGH)
time.sleep(10)