import RPi.GPIO as GPIO
import pygame
import time
import os
from pathlib import Path

current_file_path = Path(__file__)
current_directory = current_file_path.parent.resolve()

# GPIO setup
# Connect 1K-10K resistor between +3.3V and the button, then the button to GPIO 10.
BUTTON_PIN = 10
GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Audio setup
pygame.mixer.init()
chime_file = current_directory / "chime.mp3"

if not chime_file.exists():
    raise FileNotFoundError(f"Chime file not found: {chime_file}")

pygame.mixer.music.load(str(chime_file))

print("Doorbell system ready. Waiting for button press...")

try:
    # Button pressed
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
            print("Ding dong!")
            pygame.mixer.music.play()
            # Debounce and prevent repeat
            time.sleep(1)
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Shutting down.")
finally:
    GPIO.cleanup()