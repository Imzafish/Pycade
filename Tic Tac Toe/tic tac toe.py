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

Red=(255,0,0)

Black=(0,0,0)


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
                
    square_pos = (25, 25)
    square_size = (25, 25)
    pygame.draw.rect(screen, Black, (square_pos[0], square_pos[1], square_size[0], square_size[1]))
    line1_start = (8, 2)
    line1_end = (8, 23)
    line2_start = (16, 2)
    line2_end = (16, 23)
    line3_start = (2, 8)
    line3_end = (23, 8)
    line4_start = (2, 16)
    line4_end = (23, 16)
    pygame.draw.line(screen, Red, line1_start, line1_end)
    pygame.draw.line(screen, Red, line2_start, line2_end)
    pygame.draw.line(screen, Red, line3_start, line3_end)
    pygame.draw.line(screen, Red, line4_start, line4_end)
    while True:
        for events in pygame.event.get():

            if events.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
            if events.type == QUIT:
    
    
    
                sys.exit(0)
main_A()
'''
Board- 25,25
Square- 25,25
Line-8,2,8,23
Line 16,2,16,23
Line 2,8,23,8
Line 2,16,23,16
'''

