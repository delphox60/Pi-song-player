import time
import pygame
import pi

pygame.init()

def play(num):
    pygame.mixer.Sound('sound/' + str(num + 25) + '.wav').play()
    time.sleep(0.7)

for digit in pi.PI:
    
    if digit == ".":
        continue
    
    play(digit)