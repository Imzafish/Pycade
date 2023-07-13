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

Red=(255,0,0)

Black=(0,0,0)


line_color = (255, 0, 0)


def draw_line(screen, line_color, start_pos, end_pos):
    # A function to draw a line on the screen
    pygame.draw.line(screen,line_color, start_pos, end_pos)

def draw_square(screen, square_color, square_pos, square_size):
    # A function to draw a square on the screen
    pygame.draw.rect(screen, square_color, (square_pos[0], square_pos[1], square_size[0], square_size[1]))

def main():
    # Create the screen object
    # The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Fill the screen with white color
    screen.fill((255,255,255))
    
    # Draw two lines on the screen
    draw_line(screen,line_color, (60, 80), (130, 100))
    draw_line(screen,line_color, (80, 60), (100, 130))

    # Draw a square on the screen
    square_pos = (25, 25)
    square_size = (25, 25)
    draw_square(screen, Black, square_pos, square_size)

    # Update the display
    pygame.display.flip()

    xTurn = True

    while True:
        for events in pygame.event.get():
            if events.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos():
                   if xTurn:
                    # draw x
                    draw_square(screen,Black,pygame.mouse.get_pos(), square_size)
                    pygame.display.flip()
                   else:
                       # draw O
                       print (filler)
                if events.type == QUIT:
                sys.exit(0)
main()

'''
Board- 25,25
Square- 25,25
Line-8,2,8,23
Line 16,2,16,23
Line 2,8,23,8
Line 2,16,23,16
'''

