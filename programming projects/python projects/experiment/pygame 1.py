#Pygame template - skeleton for a new pygame project
import pygame
import random
import os

WIDTH = 360
HEIGHT = 480
FPS = 30

#define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

#set up assets
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")
#initialize pygame and create window
pygame.init()
#mixer handle all the sound in the game
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

#Game Loop
running = True
while running:
    #keep looping at the right speed
    clock.tick(FPS)
    #process input
    for event in pygame.event.get():
        #check for closing the window
        if event.type == pygame.QUIT:
            running = False
    #update
    all_sprites.update()


    #draw or render section
    screen.fill(BLACK)
    all_sprites.draw(screen)
    #after drawing everything, flip the display
    pygame.display.flip()

pygame.quit()


