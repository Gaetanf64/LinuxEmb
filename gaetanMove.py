# Import des modules
import RPi.GPIO as GPIO
import time

# Initialisation des LED
rouge = 33
vert = 37
jaune = 35

# Initialisation de le LED verte
GPIO.setmode(GPIO.BOARD)
GPIO.setup(vert, GPIO.OUT,initial = GPIO.LOW)

GPIO.output(vert,GPIO.HIGH)
time.sleep(10)

# Initialisation de le LED jaune
GPIO.setmode(GPIO.BOARD)
GPIO.setup(jaune, GPIO.OUT,initial = GPIO.LOW)

GPIO.output(jaune,GPIO.HIGH)
time.sleep(10)

# Initialisation de le LED rouge
GPIO.setmode(GPIO.BOARD)
GPIO.setup(rouge, GPIO.OUT,initial = GPIO.LOW)

GPIO.output(rouge,GPIO.HIGH)
time.sleep(10)



GPIO.output(vert,GPIO.LOW)
GPIO.output(jaune,GPIO.LOW)
GPIO.output(rouge,GPIO.LOW)


# state = GPIO.input(LED) #Lit l'état actuel du GPIO, vrai si allumé, faux si éteint

# if state : #Si GPIO allumé
#     GPIO.output(LED, GPIO.LOW) #On l’éteint
# else : #Sinon
#     GPIO.output(LED, GPIO.HIGH) #On l'allume