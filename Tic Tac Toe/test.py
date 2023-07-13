import pygame
from pygame.locals import *


pygame.init()
pygame.font.init()

font = pygame.font.SysFont("Courier New", 40)

running = True

screen = pygame.display.set_mode((450, 500))
screen.fill("brown")

message = font.render("Hello World!!", True, ("blue"))
screen.blit(message,(0,0))

pygame.display.update()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()