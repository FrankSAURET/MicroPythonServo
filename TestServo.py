from servo import Servo
from time import sleep

# Créer un objet Servo 
servo=Servo(pin=12, min=500, max=2500, max_angle=180)
""" Servo(pin, min, max)
    pin: Le numéro du GPIO sur lequel est connecté le servomoteur.
    min (optionnel) : la largeur d'impulsion, en microsecondes, correspondant à l'angle minimum (0 degré) du servo (par défaut 500).
    max (optionnel) : la largeur d'impulsion, en microsecondes, correspondant à l'angle maximum (180 degrés) du servo (par défaut 2500).
    max_angle (optionnel) : Angle maximum du servomoteur (par défaut 180).

    On trouve ces informations sur la datasheet du servo c'est en μs.
    FT5330M : min = 500, max = 2 500, neutre = 1 500. 
    FS90 : min = 500, max = 2 500, neutre = 1 500. 
"""

while True:
    # Servo à 0 degrés
    servo.move(0)
    sleep(2)
    # Servo à 90 degrés
    servo.move(90)
    sleep(2)
    # Servo à 180 degrés
    servo.move(180)
    sleep(2)
        
