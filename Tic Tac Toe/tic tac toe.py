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
#Keep it a square for it to work about 450x450 is a good size
SCREEN_WIDTH = 450
SCREEN_HEIGHT = 450
A=SCREEN_HEIGHT//3
B=SCREEN_HEIGHT//3

Y=SCREEN_HEIGHT//6
X=SCREEN_WIDTH//6
print(str(X),"\n" + str(Y))
Box_Center_1=(X*5,Y*1)
Box_Center_2=(X*3,Y*1)
Box_Center_3=(X*1,Y*1)
Box_Center_4=(X*5,Y*3)
Box_Center_5=(X*3,Y*3)
Box_Center_6=(X*1,Y*3)
Box_Center_7=(X*5,Y*5)
Box_Center_8=(X*3,Y*5)
Box_Center_9=(X*1,Y*5)


filled_squares = [['MT', 'MT', 'MT'], ['MT', 'MT', 'MT'], ['MT', 'MT', 'MT']]


'''
With 
SCREEN_WIDTH = 450
SCREEN_HEIGHT = 450
these are centers
|375,75 |225,75 |75,75 |
|375,255|225,225|75,225|
|375,375|225,376|75,375|
'''


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
    print("Grid drawing")
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
    
def draw_X(screen, line_color, start_pos, end_pos):
    # A function to draw a X on the screen
    pygame.draw.lines(screen, Black, True, [(start_pos[0]-50,start_pos[1]-50),(start_pos[0]+50,start_pos[1]+50)], 3)
    pygame.draw.lines(screen, Black, True, [(start_pos[0]-50,start_pos[1]+50),(start_pos[0]+50,start_pos[1]-50)], 3)
    pygame.display.flip()

def draw_0(screen, color, center, width):
    # A function to draw a ring on the screen
    #pygame.draw.circle(screen, color, center, radius, width)
    pygame.draw.circle(screen, (0, 0, 0), center, 50, 2)
    pygame.display.flip()

def win_function():
    if filled_squares[0][0] == filled_squares [0][1] == filled_squares [0][2]:
        if filled_squares[0][0]=="X":
            print("X wins the game")
        elif filled_squares[0][0]=="0":
            print("0 wins the game")
    elif filled_squares[1][0] == filled_squares [1][1] == filled_squares [1][2]:
        if filled_squares[1][0]=="X":
            print("X wins the game")
        elif filled_squares[1][0]=="0":
            print("0 wins the game")
    elif filled_squares [2][0] == filled_squares [2][1] == filled_squares [2][2]:
        if filled_squares [2][0]=="X":
            print("X wins the game")
        elif filled_squares [2][0]=="0":
            print("0 wins the game")
    elif filled_squares [0][0] == filled_squares [1][1] == filled_squares [2][2]:
        if filled_squares [0][0]=="X":
            print("X wins the game")
        elif filled_squares [0][0]=="0":
            print("0 wins the game")
    elif filled_squares [0][2] == filled_squares [1][1] == filled_squares [20][20]:
        if filled_squares [0][2]=="X":
            print("X wins the game")
        elif filled_squares [0][2]=="0":
            print("0 wins the game")
    elif filled_squares [0][0] == filled_squares [1][0] == filled_squares [2][0]:
        if filled_squares [0][0]=="X":
            print("X wins the game")
        elif filled_squares [0][0]=="0":
            print("0 wins the game")
    elif filled_squares [1][0] == filled_squares [1][1] == filled_squares [2][1]:
        if filled_squares [1][0]=="X":
            print("X wins the game")
        elif filled_squares [1][0]=="0":
            print("0 wins the game")
    elif filled_squares [0][2] == filled_squares [1][2] == filled_squares [2][2]:
        if filled_squares [0][2]=="X":
            print("X wins the game")
        elif filled_squares [0][2]=="0":
            print("0 wins the game")

#If turn is True its X turn, otherwise its O turn
def findPos(turn):
    var = pygame.mouse.get_pos()[0]
    var2 = pygame.mouse.get_pos()[1]
    if var <= 150:
        if var2 <= 150:
            print("Top Left")

            if turn:
                filled_squares[0][0]="X"
            else:
                filled_squares[0][0]="O"

           
            return Box_Center_3
        elif var2 <= 300:
            print("Mid Left")
            {True: filled_squares[1][0]=="X", False: filled_squares[1][0]=="O"}[turn]
            return Box_Center_6
            
        else:
            print("Bottom Left")
            {True: filled_squares[2][0]=="X", False: filled_squares[2][0]=="O"}[turn]
            return Box_Center_9
    elif var <= 300:
        if var2 <= 150:
            print("Top Mid")
            {True: filled_squares[0][1]=="X", False: filled_squares[0][1]=="O"}[turn]
            return Box_Center_2
        elif var2 <= 300:
            print("Mid Mid")
            {True: filled_squares[1][1]=="X", False: filled_squares[1][1]=="O"}[turn]
            return Box_Center_5
        else:
            print("Bottom Mid")
            {True: filled_squares[2][1]=="X", False: filled_squares[2][1]=="O"}[turn]
            return Box_Center_8
    else:
        if var2 <= 150:
            print("Top Right")
            {True: filled_squares[0][2]=="X", False: filled_squares[0][2]=="O"}[turn]
            return Box_Center_1
        elif var2 <= 300:
            print("Mid Right")
            {True: filled_squares[1][2]=="X", False: filled_squares[1][2]=="O"}[turn]
            return Box_Center_4
        else:
            print("Bottom Right")
            {True: filled_squares[2][2]=="X", False: filled_squares[2][2]=="O"}[turn]
            return Box_Center_7

def main():
    xTurn = True
    while True:
        for events in pygame.event.get():
            if events.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos():
                   if xTurn:
                        # draw x 
                        draw_X(screen,Black,findPos(True), square_size)
                        xTurn = False
                   else:
                        # draw O
                        draw_0(screen,Black,findPos(False), width=0)
                        xTurn = True
                win_function()
                print(filled_squares)
            if events.type == QUIT:
                sys.exit(0)

# Call the main function
grid_draw()
main()
grid_draw()
main()












'''
Board- 25,25
Square- 25,25
Line-8,2,8,23
Line 16,2,16,23
Line 2,8,23,8
Line 2,16,23,16
'''
'''Middle box center 75,75'''
