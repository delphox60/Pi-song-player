import time
import pygame
import pi

pygame.init()

INTERVAL = 0.3
DEFAULT_OFFSET = 25

stair_nums = [25, 27, 29, 30, 32, 34, 36, 37, 39]

def get_stair_num(n):
    
    return stair_nums[n - 1]


def play(num):
    pygame.mixer.Sound('sound/' + str(get_stair_num(num)) + '.wav').play()
    time.sleep(INTERVAL)

for digit in pi.PI:
    
    if digit == ".":
        continue
    
    if digit == "0" or digit == "9":
        # time.sleep(DEFAULT_OFFSET)
        continue
    
    play(int(digit))