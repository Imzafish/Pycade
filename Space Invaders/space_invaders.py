### GAMEMODE OF SPACE INVADERS 
# Initialize Pygame
import pygame
import random
import time

pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")

# Set up the player
player_image = pygame.image.load("player.png")
player_rect = player_image.get_rect()
player_rect.centerx = 400
player_rect.bottom = 580
player_speed = 5

# Set up the enemy
enemy_image = pygame.image.load("enemy.png")
enemy_rect = enemy_image.get_rect()
enemy_rect.centerx = random.randint(50, 750)
enemy_rect.centery = random.randint(50, 150)
enemy_speed = 3

# Set up the bullet
bullet_image = pygame.image.load("bullet.png")
bullet_rect = bullet_image.get_rect()
bullet_speed = 10
bullet_state = "ready"

# Set up the score
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
text_x = 10
text_y = 10

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def player(x, y):
    screen.blit(player_image, (x, y))

def enemy(x, y):
    screen.blit(enemy_image, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_image, (x + 16, y + 10))

def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = ((enemy_x - bullet_x) ** 2 + (enemy_y - bullet_y) ** 2) ** 0.5
    if distance < 27:
        return True
    else:
        return False

# Set up the game over text
game_over_font = pygame.font.Font("freesansbold.ttf", 64)

def game_over_text():
    game_over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(game_over_text, (200, 250))

# Set up the game loop
running = True
while running:

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Move the player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_rect.centerx -= player_speed
            if event.key == pygame.K_RIGHT:
                player_rect.centerx += player_speed
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = pygame.mixer.Sound("laser.wav")
                    bullet_sound.play()
                    bullet_rect.centerx = player_rect.centerx
                    bullet_rect.bottom = player_rect.top
                    fire_bullet(bullet_rect.centerx, bullet_rect.top)

    # Move the enemy
    enemy_rect.centerx += enemy_speed
    if enemy_rect.left < 0 or enemy_rect.right > 800:
        enemy_speed = -enemy_speed
        enemy_rect.centery += 50

    # Move the bullet
    if bullet_rect.bottom < 0:
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bullet_rect.centerx, bullet_rect.top)
        bullet_rect.top -= bullet_speed

    # Check for collision
    if is_collision(enemy_rect.centerx, enemy_rect.centery, bullet_rect.centerx, bullet_rect.top):
        explosion_sound
