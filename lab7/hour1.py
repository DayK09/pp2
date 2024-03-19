import pygame
import math
from datetime import datetime

pygame.init()

screen = pygame.display.set_mode((830, 800))
pygame.display.set_caption('Clock')
clock = pygame.time.Clock()
main = pygame.image.load('lab7/main-clock.png')
right = pygame.image.load('lab7/right-hand.png')
left = pygame.image.load('lab7/left-hand.png')

def time():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        ctime = datetime.now()
        hour, minute = ctime.hour % 12, ctime.minute 
        
        # Рассчитываем углы в градусах
        minute_angle = minute *4 
        hour_angle = hour * 25 
        
        screen.fill((255, 255, 255))
        screen.blit(main, (0, 0))
        
        rotated_right = pygame.transform.rotate(right, -hour_angle)
        right_rect = rotated_right.get_rect(center=(415, 400))
        screen.blit(rotated_right, right_rect)
       
        rotated_left = pygame.transform.rotate(left, -minute_angle)
        left_rect = rotated_left.get_rect(center=(415, 400))
        screen.blit(rotated_left, left_rect)

        pygame.display.update()
        clock.tick(60)

time()
pygame.quit()
