import pygame
import math
from datetime import datetime

pygame.init()

screen = pygame.display.set_mode((830, 800))
pygame.display.set_caption('Clock')
clock = pygame.time.Clock()
main = pygame.image.load('main-clock.png')
right = pygame.image.load('right-hand.png')
left = pygame.image.load('left-hand.png')

def rot_center(image, angle, x, y):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(center=(x, y)).center)
    return rotated_image, new_rect

def run_clock():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        current_time = datetime.now()
        hour = current_time.hour % 12
        minute = current_time.minute
        
        # Calculate angles in degrees
        minute_angle = minute * 6  # 360 degrees divided by 60 minutes
        hour_angle = (hour * 30) + (minute / 2)  # 360 degrees divided by 12 hours + (30 degrees divided by 60 minutes)
        
        screen.fill((255, 255, 255))
        screen.blit(main, (0, 0))
        
        rotated_right, right_rect = rot_center(right, -hour_angle + 90, 415, 400)
        screen.blit(rotated_right, right_rect)
       
        rotated_left, left_rect = rot_center(left, -minute_angle + 90, 415, 400)
        screen.blit(rotated_left, left_rect)

        pygame.display.update()
        clock.tick(60)

run_clock()
pygame.quit()
