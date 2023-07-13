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
Red=(255,0,0)

Black=(0,0,0)
def grid_draw():
    print("Grid")
    # Draw the tic-tac-toe grid
    line_color = (0, 0, 0)  # Black
    line_width = 5

    # Vertical lines
    pygame.draw.line(screen, line_color, (SCREEN_WIDTH // 3, 0), (SCREEN_WIDTH // 3, SCREEN_HEIGHT), line_width)
    pygame.draw.line(screen, line_color, (2 * SCREEN_WIDTH // 3, 0), (2 * SCREEN_WIDTH // 3, SCREEN_HEIGHT), line_width)

    # Horizontal lines
    pygame.draw.line(screen, line_color, (0, SCREEN_HEIGHT // 3), (SCREEN_WIDTH, SCREEN_HEIGHT // 3), line_width)
    pygame.draw.line(screen, line_color, (0, 2 * SCREEN_HEIGHT // 3), (SCREEN_WIDTH, 2 * SCREEN_HEIGHT // 3), line_width)

    # Update the display
    pygame.display.flip()
        
grid_draw()

def draw_X(screen, line_color, start_pos, end_pos):
    # A function to draw a X on the screen
    pygame.draw.lines(screen, Black, True, [(start_pos[0]-50,start_pos[1]-50),(start_pos[0]+50,start_pos[1]+50)], 3)
    pygame.draw.lines(screen, Black, True, [(start_pos[0]-50,start_pos[1]+50),(start_pos[0]+50,start_pos[1]-50)], 3)
    pygame.display.flip()

def draw_0(screen, Black, O_pos, width):
    # A function to draw an 0 on the screen
    pygame.draw.circle(screen, Black,O_pos,50, width=490)
    pygame.display.flip()
def main():
    xTurn = True

    while True:
        for events in pygame.event.get():
            if events.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos():
                   if xTurn:
                    # draw x
                    draw_X(screen,Black,pygame.mouse.get_pos(), square_size)
                    xTurn = False
                   else:
                       # draw O
                       draw_0(screen,Black,pygame.mouse.get_pos(), width=0)
                       
                       xTurn = True
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

