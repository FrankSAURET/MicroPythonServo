<div style="text-align: right"><a href="#servo-library-for-raspberry-pi-pico">English</a></div>

# Bibliothèque Servo pour Raspberry Pi Pico 

## Description
Cette bibliothèque MicroPython permet de contrôler facilement des servomoteurs avec le Raspberry Pi Pico. Elle gère automatiquement la génération des signaux PWM nécessaires pour positionner précisément un servomoteur.

## Caractéristiques
- Contrôle de la position angulaire (0° à 180° par défaut)
- Configuration personnalisable des largeurs d'impulsions
- Méthodes simples pour positionner et arrêter le servomoteur

## Installation
Copiez simplement le fichier `servo.py` dans votre projet MicroPython sur le Micro Python.

## Utilisation

```python
from servo import Servo
from time import sleep

# Création d'un servomoteur sur la broche GPIO 12
servo = Servo(pin=12)

# Positionner le servo à 90°
servo.move(90)

# Arrêter le servo
servo.stop()
```

## API

### Constructeur

```python
Servo(pin, min=500, max=2500, max_angle=180)
```

| Paramètre | Description |
|-----------|-------------|
| `pin` | Le numéro de la broche GPIO du Micro Python connectée au servomoteur |
| `min` | La largeur d'impulsion en microsecondes correspondant à l'angle minimum (0°), par défaut 500μs |
| `max` | La largeur d'impulsion en microsecondes correspondant à l'angle maximum, par défaut 2500μs |
| `max_angle` | Angle maximum du servomoteur en degrés, par défaut 180° |

### Méthodes

| Méthode | Description |
|---------|-------------|
| `move(angle)` | Positionne le servomoteur à l'angle spécifié en degrés |
| `stop()` | Arrête le signal PWM et libère le servomoteur |
| `get_angle()` | Retourne l'angle actuel du servomoteur |

## Exemple complet

```python
from servo import Servo
from time import sleep

# Créer un objet Servo avec configuration personnalisée
servo = Servo(pin=12, min=500, max=2500, max_angle=180)

# Servo à 0 degrés
servo.move(0)
sleep(2)
# Servo à 90 degrés
servo.move(90)
sleep(2)
# Servo à 180 degrés
servo.move(180)
sleep(2)
        
```

## Auteur
Frank SAURET, basé sur le travail de Rui Santos & Sara Santos (Random Nerd Tutorials)

---

# Servo Library for Raspberry Pi Pico

## Description
This MicroPython library allows easy control of servo motors with the Raspberry Pi Pico. It automatically manages the generation of PWM signals needed to precisely position a servo motor.

## Features
- Control of angular position (0° to 180° by default)
- Customizable pulse width configuration
- Simple methods to position and stop the servo motor

## Installation
Simply copy the `servo.py` file into your MicroPython project on the Raspberry Pi Pico.

## Usage

```python
from servo import Servo
from time import sleep

# Create a servo on GPIO pin 12
servo = Servo(pin=12)

# Position the servo at 90°
servo.move(90)

# Stop the servo
servo.stop()
```

## API

### Constructor

```python
Servo(pin, min=500, max=2500, max_angle=180)
```

| Parameter | Description |
|-----------|-------------|
| `pin` | The GPIO pin number of the Raspberry Pi Pico connected to the servo motor |
| `min` | The pulse width in microseconds corresponding to the minimum angle (0°), default 500μs |
| `max` | The pulse width in microseconds corresponding to the maximum angle, default 2500μs |
| `max_angle` | Maximum angle of the servo motor in degrees, default 180° |

### Methods

| Method | Description |
|---------|-------------|
| `move(angle)` | Positions the servo motor at the specified angle in degrees |
| `stop()` | Stops the PWM signal and releases the servo motor |
| `get_angle()` | Returns the current angle of the servo motor |

## Compatible Servo Motors Examples

| Model | min (μs) | max (μs) | neutral (μs) |
|--------|----------|----------|-------------|
| FT5330M | 500 | 2500 | 1500 |
| FS90 | 500 | 2500 | 1500 |

## Complete Example

```python
from servo import Servo
from time import sleep

# Create a Servo object with custom configuration
servo = Servo(pin=12, min=500, max=2500, max_angle=180)

try:
    while True:
        # Servo at 0 degrees
        servo.move(0)
        sleep(2)
        # Servo at 90 degrees
        servo.move(90)
        sleep(2)
        # Servo at 180 degrees
        servo.move(180)
        sleep(2)
        
except KeyboardInterrupt:
    print("Keyboard interrupt")
    # Turn off PWM
    servo.stop()
```

## Author
Frank SAURET, based on the work of Rui Santos & Sara Santos (Random Nerd Tutorials)