import pygame
from time import*
from pygame.locals import*

pygame.init()
width = 800
height = 650
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("rocket")

image1 = pygame.image.load("rocket.png")
image2 = pygame.image.load("space.png")
image1_x = 200
image1_y = 200
keys = [False, False , False, False]

while image1_y < 800:

    screen.blit(image2, (0,0))
    screen.blit(image1,(image1_x,image1_y))
    pygame.display.update()

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
        if i.type == pygame.KEYDOWN:
            if i.key == K_UP:
                keys[0] = True
            elif i.key == K_LEFT:
                keys[1] = True
            elif i.key == K_DOWN:
                keys[2] = True
            elif i.key == K_RIGHT:
                keys[3] = True
        if i.type == pygame.KEYUP:
            if i.key == K_UP:
                keys[0] = False
            elif i.key == K_LEFT:
                keys[1] = False
            elif i.key == K_DOWN:
                keys[2] = False
            elif i.key == K_RIGHT:
                keys[3] = False
            
    if keys[0]:
        if image1_y > 0:
            image1_y -= 7
    elif keys[2]:
        if image1_y < 600:
            image1_y += 7
    
    if keys[1]:
        if image1_x > 0:
            image1_x -= 7
    elif keys[3]:
        if image1_x < 750:
            image1_x += 7
    
    image1_y += 5
    sleep(0.05)

print("gameover")
font = pygame.font.SysFont("Arial", 52)
text = font.render("game over",True,"blue")
pygame.display.update()
sleep(2)

pygame.quit()