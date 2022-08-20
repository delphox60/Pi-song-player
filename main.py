from cmath import pi
import time
from xml.etree.ElementTree import PI
import pygame

pygame.init()

def play(num):
    pygame.mixer.Sound('sound/' + str(num + 25) + '.wav').play()
    time.sleep(0.7)
