import pygame
import os

pygame.mixer.init()
audio_path = os.path.abspath("assets/audio/1.wav")  # Replace with an actual path
print(f"Playing: {audio_path}")
pygame.mixer.music.load(audio_path)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pass