


import RPi.GPIO as GPIO
import time
rouge = 33
jaune= 35
vert =37
capteur= 38
# Initialisation de la numerotation et des E/S
GPIO.setmode(GPIO.BOARD)
GPIO.setup(jaune, GPIO.OUT)
GPIO.setup(capteur, GPIO.IN)
while(True):
        if GPIO.input(capteur)==False:
                print("fonctionne")
        else:
                print("ne fonctionne pas")


        time.sleep(0.5)

