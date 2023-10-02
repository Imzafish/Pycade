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

import pygame

pygame.init()
screen_info = pygame.display.Info()

width = screen_info.current_w
height = screen_info.current_h

print("Screen size: {}x{}".format(width, height))
player1_paddle = Paddle(175, 400)
player2_paddle = Paddle(175, 40)
pygame.quit()
Black=(0,0,0)
initial_ball_speed=1
game_over = False
def reset_ball_position():
    global ball_x, ball_y
    ball_x, ball_y = square_pos / 2, square_size / 2
    ball_vx, ball_vy = initial_ball_speed, initial_ball_speed
    game_over = False
    pygame.display.flip()
    
reset_ball_position()

print(ball_x, ball_y)
def ball_hits_paddle():
    ball_vx *= -1  # Reverse horizontal velocity, really intreasting maths in this


if paddle_collision==True:
    ball_hits_paddle()
    
else:
    print("No collision")

def handle_input(ball_mechanics):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
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
    elif ball_hits_wall():
        ball_vy *= -1  # Reverse vertical velocity
    elif ball_out_of_bounds():
        if ball_x < 0:
            player2_score += 1
        else:
            player1_score += 1
        reset_ball_position()

    # Render game state

