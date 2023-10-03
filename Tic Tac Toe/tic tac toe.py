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
#Win statement
filled_squares = [['MT', 'MT', 'MT'], ['X', 'MT', 'MT'], ['MT', 'MT', 'MT']]
def win_function():
    if filled_squares[0][0] and filled_squares [0][1] and filled_squares [0][2]=="X" or "0":
        if filled_squares[0][0]=="X":
            print("X wins the game")
        elif filled_squares[0][0]=="0":
            print("0 wins the game")
    elif filled_squares[1][0] and filled_squares [1][1] and filled_squares [1][2]=="X" or "0":
        if filled_squares[1][0]=="X":
            print("X wins the game")
        elif filled_squares[1][0]=="0":
            print("0 wins the game")
    elif filled_squares [2][0] and filled_squares [2][1] and filled_squares [2][2]=="X" or "0":
        if filled_squares [2][0]=="X":
            print("X wins the game")
        elif filled_squares [2][0]=="0":
            print("0 wins the game")
    elif filled_squares [0][0] and filled_squares [1][1] and filled_squares [2][2]=="X" or "0":
        if filled_squares [0][0]=="X":
            print("X wins the game")
        elif filled_squares [0][0]=="0":
            print("0 wins the game")
    elif filled_squares [0][2] and filled_squares [1][1] and filled_squares [20][20]=="X" or "0":
        if filled_squares [0][2]=="X":
            print("X wins the game")
        elif filled_squares [0][2]=="0":
            print("0 wins the game")
    elif filled_squares [0][0] and filled_squares [1][0] and filled_squares [2][0]=="X" or "0":
        if filled_squares [0][0]=="X":
            print("X wins the game")
        elif filled_squares [0][0]=="0":
            print("0 wins the game")
    elif filled_squares [1][0] and filled_squares [1][1] and filled_squares [2][1]=="X" or "0":
        if filled_squares [1][0]=="X":
            print("X wins the game")
        elif filled_squares [1][0]=="0":
            print("0 wins the game")
    elif filled_squares [0][2] and filled_squares [1][2] and filled_squares [2][2]=="X" or "0":
        if filled_squares [0][2]=="X":
            print("X wins the game")
        elif filled_squares [0][2]=="0":
            print("0 wins the game")
win_function()
def draw_0(screen, color, center, width):
    # A function to draw a ring on the screen
    #pygame.draw.circle(screen, color, center, radius, width)
    pygame.draw.circle(screen, (0, 0, 0), pygame.mouse.get_pos(), 50, 2)
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

   


win_function()



'''
Board- 25,25
Square- 25,25
Line-8,2,8,23
Line 16,2,16,23
Line 2,8,23,8
Line 2,16,23,16
'''

'''def main():
    xTurn = True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos():
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    # Determine the grid position by dividing into thirds
                    if mouse_x < SCREEN_WIDTH // 3:
                        col = 0
                    elif mouse_x < 2 * SCREEN_WIDTH // 3:
                        col = 1
                    else:
                        col = 2
                    if mouse_y < SCREEN_HEIGHT // 3:
                        row = 0
                    elif mouse_y < 2 * SCREEN_HEIGHT // 3:
                        row = 1
                    else:
                        row = 2
                    # Update the filled_squares matrix
                    if xTurn:
                        filled_squares[row][col] = 'X'
                        draw_X(screen, Black, (col * SCREEN_WIDTH // 3 + SCREEN_WIDTH // 6, row * SCREEN_HEIGHT // 3 + SCREEN_HEIGHT // 6), square_size)
                        xTurn = False
                    else:
                        filled_squares[row][col] = 'O'
                        draw_0(screen, Black, (col * SCREEN_WIDTH // 3 + SCREEN_WIDTH // 6, row * SCREEN_HEIGHT // 3 + SCREEN_HEIGHT // 6), width=0)
                        xTurn = True
            if event.type == QUIT:
                sys.exit(0)
        pygame.display.update()'''