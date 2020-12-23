from sys import exit
import pygame
#you have always to do this when starting pygame
pygame.init()
#create a window and window size
win = pygame.display.set_mode((500, 500))


pygame.display.set_caption("First Game")

#size of the character that you want to move
x = 225
y = 225
width = 40
height  = 60
vel = 5

isJump = False
jumpcount = 10

run = True
while run:
    #to limit the move of the character to be slow
    pygame.time.delay(25)
    # mouse position and keyboard position
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #moving the rectangle
    #engine
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    #if we want to prevent we make sure the character looks like he's not moving off the screen we just need to subract the width of the character
    if keys[pygame.K_RIGHT] and x < 500 - width -vel:
        x += vel
    if not (isJump):
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < 500 - height - vel:
            y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpcount >= -10:
            neg = 5
            if jumpcount < 0:
                neg = -5
            y -= (jumpcount ** 2) * 0.5 * neg
            jumpcount =- 1
        else:
            isJump = False
            jumpcount = 10



    #we need to fill the screen so there won't be any trace to the color
    win.fill((0, 0, 0))
    #screen, color, (x,y,width,height), thickness) draws a rectangle (x,y,width,height)
    #or engine of the character
    pygame.draw.rect(win, (255, 0, 0), (x , y, width, height))
    #to refresh the display
    pygame.display.update()

pygame.quit()




