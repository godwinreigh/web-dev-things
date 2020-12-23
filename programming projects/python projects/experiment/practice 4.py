import pygame
pygame.init()
win =pygame.display.set_mode((500, 500))

pygame.display.set_caption("PRACTICE")

x= 225
y = 225
width = 40
height = 60
vel = 1

#jump functionality
jump = False
jump_count = 10
#quit button
run = True
while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



    #character
    win.fill((0, 0, 0))
    pygame.draw.rect(win,(0,0,255), (x, y, width,height))
    pygame.display.update()

    # keys functionality
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 500 - width - vel:
            x += vel
    if keys[pygame.K_UP] and y > vel:
            y -= vel
    if keys[pygame.K_DOWN] and y < 500 -height -vel:
            y += vel
    if keys [pygame.K_SPACE]:
        jump_count = (0.5 * jump_count * (vel*vel))
        








pygame.quit()