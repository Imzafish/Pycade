import random
import time
import pygame
import sys
from pygame.locals import *

# Start Pygame
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
screen.fill((255, 255, 255))

square_pos = (25, 25)
square_size = (25, 25)

# Update the display
pygame.display.flip()

# Initialize ball position, velocity, and scores
ball_x, ball_y = square_pos[0] / 2, square_size[1] / 2
ball_vx, ball_vy = 1, 1  # initial_ball_speed
player1_score, player2_score = 0, 0

# Define paddle class
class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.direction = 0

    def move(self):
        self.x += self.direction * self.speed

    def draw(self):
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, 100, 10))

    def move_left(self):
        self.direction = -1

    def move_right(self):
        self.direction = 1

    def stop(self):
        self.direction = 0

# Create paddles
player1_paddle = Paddle(175, 400)
player2_paddle = Paddle(175, 40)

# Function to handle paddle-ball collision
def ball_hits_paddle(paddle):
    if paddle.x <= ball_x <= paddle.x + 100 and paddle.y <= ball_y <= paddle.y + 10:
        return True
    return False

# Function to handle ball-wall collision
def ball_hits_wall():
    if ball_x <= 0 or ball_x >= SCREEN_WIDTH - square_size[0]:
        return True
    return False

# Function to check if ball is out of bounds
def ball_out_of_bounds():
    if ball_y <= 0 or ball_y >= SCREEN_HEIGHT - square_size[1]:
        return True
    return False

# Function to reset ball position and velocity
def reset_ball_position():
    global ball_x, ball_y, ball_vx, ball_vy
    ball_x, ball_y = square_pos[0] / 2, square_size[1] / 2
    ball_vx, ball_vy = 1, 1  # initial_ball_speed
    pygame.display.flip()

# Game loop
game_over = False
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player1_paddle.move_left()
            if event.key == pygame.K_RIGHT:
                player1_paddle.move_right()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player1_paddle.stop()

    # Update paddle positions
    player1_paddle.move()

    # Update ball position
    ball_x += ball_vx
    ball_y += ball_vy

    # Check for collisions
    if ball_hits_paddle(player1_paddle) or ball_hits_paddle(player2_paddle):
        ball_vy *= -1  # Reverse vertical velocity

    elif ball_hits_wall():
        ball_vx *= -1  # Reverse horizontal velocity

    elif ball_out_of_bounds():
        if ball_y < 0:
            player2_score += 1
        else:
            player1_score += 1
        reset_ball_position()

    # Render game state
    screen.fill((255, 255, 255))
    player1_paddle.draw()
    player2_paddle.draw()
    pygame.draw.rect(screen, (0, 0, 0), (ball_x, ball_y, square_size[0], square_size[1]))
    pygame.display.flip()

    clock.tick(60)