# Import des modules
import RPi.GPIO as GPIO
import time

# Initialisation des LED et du capteur
rouge = 33
vert = 37
jaune = 35
capteur= 38

# Initialisation du setup de la LED verte
GPIO.setmode(GPIO.BOARD)
GPIO.setup(vert, GPIO.OUT,initial = GPIO.HIGH)

# Initialisation du setup de la LED jaune
GPIO.setmode(GPIO.BOARD)
GPIO.setup(jaune, GPIO.OUT,initial = GPIO.LOW)

# Initialisation du setup de la LED rouge
GPIO.setmode(GPIO.BOARD)
GPIO.setup(rouge, GPIO.OUT,initial = GPIO.LOW)

# Initialisation du setup du capteur
GPIO.setmode(GPIO.BOARD)
GPIO.setup(capteur, GPIO.IN)


# Boucle qui fonctionne tant que le programme est exécuté
while(True):
    # LED verte active de base
    GPIO.output(vert, GPIO.HIGH)

    # Si le capteur détecte un mouvement
    if GPIO.input(capteur)==False:
        # On modifie les LED : la jaune s'allume et la verte s'éteind
        GPIO.output(vert, GPIO.LOW)
        GPIO.output(jaune, GPIO.HIGH)
        time.sleep(0.5)
        
        # Tant que le capteur détecte un mouvement continu
        while GPIO.input(capteur)==False:
            # On modifie les LED : la rouge s'allume et la jaune s'éteind
            GPIO.output(jaune, GPIO.LOW)
            GPIO.output(rouge, GPIO.HIGH)
            time.sleep(1.5)
        # Une fois la boucle while terminée, on coupe les LED rouge et jaune
        GPIO.output(jaune, GPIO.LOW)
        GPIO.output(rouge, GPIO.LOW)
    time.sleep(0.05)  # Pause pour ne pas saturer le processeur


# On éteind toutes les LED
GPIO.output(jaune, GPIO.LOW)
GPIO.output(rouge, GPIO.LOW)
GPIO.output(vert, GPIO.LOW)