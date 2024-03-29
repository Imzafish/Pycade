import random
import time
import pygame,sys
from pygame.locals import *
# Define paddle class
pygame.quit()
class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self):
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, 100, 10))

player1_score=0
player2_score=0
    
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

# Initialize ball position, velocity, and scores
ball_x, ball_y = square_pos[0] / 2, square_size[1] / 2
ball_vx, ball_vy = 1, 1  # initial_ball_speed
player1_score, player2_score = 0, 0
import pygame

pygame.init()
screen_info = pygame.display.Info()

width = screen_info.current_w
height = screen_info.current_h

print("Screen size: {}x{}".format(width, height))


player1_paddle =Paddle(175, 400)
player2_paddle = Paddle(175, 40)
#Learn a class?
#Looking at a friends code and saw classes
pygame.quit()
Black=(0,0,0)
initial_ball_speed=1
game_over = False
print(ball_x, ball_y)
def ball_hits_paddle():
    ball_vx *= -1  # Reverse horizontal velocity, really intreasting maths in this

paddle_collision=False

if paddle_collision==True:
    ball_hits_paddle() 
else:
    print("No collision")

def handle_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player1_paddle.move_left()
                if event.key == pygame.K_RIGHT:
                    player1_paddle.move_right()
                if event.key == pygame.K_UP:
                    player2_paddle.move_up()
                if event.key == pygame.K_DOWN:
                    player2_paddle.move_down()
                if event.type == pygame.KEYUP:
                    print("hi")
                if event.key == pygame.K_LEFT:
                    player1_paddle.stop_left()
                if event.key == pygame.K_RIGHT:
                    player1_paddle.stop_right()
                if event.key == pygame.K_UP:
                    player2_paddle.stop_up()
                if event.key == pygame.K_DOWN:
                    player2_paddle.stop_down()

# Game loop
while not game_over:
    # Handle input to move paddles
    handle_input()

 # Update ball position
    ball_x += ball_vx
    ball_y += ball_vy

    # Check for collisions
    if ball_hits_paddle(player1_paddle) or ball_hits_paddle(player2_paddle):
        ball_vx *= -1  # Reverse horizontal velocity
       # Render game state

