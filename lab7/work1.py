import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('play')
clock = pygame.time.Clock()
x = 250
y = 250
r = 25
vel = 20

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    
    user = pygame.key.get_pressed()

    if user[pygame.K_LEFT]:
        x -= vel
    if user[pygame.K_RIGHT]:
        x += vel
    if user[pygame.K_UP]:
        y -= vel
    if user[pygame.K_DOWN]:
        y += vel

    if x > 485: 
        x -= 20
    if y > 485: 
        y -= 20
    if x < 20: 
        x += 20
    if y < 20: 
        y += 20


    screen.fill((255, 255, 255))  
    pygame.draw.circle(screen, (255, 0, 0), (int(x), int(y)), r)  
    pygame.display.update()  
    clock.tick(60)
