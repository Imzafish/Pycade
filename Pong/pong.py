import random
import time
import pygame,sys
from pygame.locals import *

#Start Pygame
pygame.font.init()
font = pygame.font.SysFont("Courier New", 40)
pygame.display.set_caption('Tic Tac Toe')
pygame.init()

# Define constants for the screen width and height
SCREEN_WIDTH = 450
SCREEN_HEIGHT = 450


    # Create the screen object
    # The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Fill the screen with white color
screen.fill((255,255,255))
square_pos = (25, 25)
square_size = (25, 25)
# Update the display
pygame.display.flip()