# Import des modules
import RPi.GPIO as GPIO
import time

# Initialisation de la numerotation et des E/S
GPIO.setmode(GPIO.BOARD)
GPIO.setup(35, GPIO.OUT, initial = GPIO.HIGH)

# On fait clignoter la LED
while True:
    GPIO.output(35, not GPIO.input(35))
    time.sleep(0.5)