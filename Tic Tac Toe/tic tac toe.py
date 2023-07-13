import random
import time
import pygame,sys
from pygame.locals import *

pygame.font.init()
font = pygame.font.SysFont("Courier New", 40)


# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
#Online website said this is important



#Start Pygame
pygame.init()

# Define constants for the screen width and height
SCREEN_WIDTH = 450
SCREEN_HEIGHT = 450
# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))






line_color = (255, 0, 0)

def main():
    screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    screen.fill((255,255,255))
    pygame.draw.line(screen,line_color, (60, 80), (130, 100))
    pygame.display.flip()

    while True:
        for events in pygame.event.get():
            if events.type == QUIT:
                sys.exit(0)

def main_A():
    screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    screen.fill((255,255,255))
    pygame.draw.line(screen,line_color, (80, 60), (100, 130))
    pygame.display.flip()

    while True:
        for events in pygame.event.get():

            if events.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
            if events.type == QUIT:
    
    
    
                sys.exit(0)
main_A()

