import pygame
from random import randrange, choice

WIDTH, HEIGHT = 1100, 700
FPS = 60
game_score = 0
paddle_w = 230
paddle_h = 25
paddle_speed = 15
ball_radius = 20
ball_speed = 6
ball_rect = int(ball_radius * 2 ** 0.5)

# Define brick types
BRICK_WIDTH = 100
BRICK_HEIGHT = 50
BRICK_COLORS = [(randrange(30, 256), randrange(30, 256), randrange(30, 256)) for _ in range(10)]
BRICK_TYPES = ["normal", "unbreakable", "bonus"]

# Initialize pygame
pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Create paddle
paddle = pygame.Rect(WIDTH // 2 - paddle_w // 2, HEIGHT - paddle_h - 10, paddle_w, paddle_h)

# Create ball
ball = pygame.Rect(randrange(ball_rect, WIDTH - ball_rect), HEIGHT // 2, ball_rect, ball_rect)
dx, dy = 1, -1

# Create bricks
block_list = [[pygame.Rect(10 + BRICK_WIDTH * i, 10 + BRICK_HEIGHT * j, BRICK_WIDTH, BRICK_HEIGHT),
               choice(BRICK_COLORS), choice(BRICK_TYPES)] for i in range(10) for j in range(4)]

def detect_collision(dx, dy, ball, rect):
    pass

def increase_ball_speed():
    global ball_speed
    ball_speed += 1

def shrink_paddle():
    global paddle_w
    if paddle_w > 50:
        paddle_w -= 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    sc.fill('black')

   
    for brick, color, brick_type in block_list:
        if brick_type != "unbreakable":
            pygame.draw.rect(sc, color, brick)

    pygame.draw.rect(sc, pygame.Color('darkorange'), paddle)
    pygame.draw.circle(sc, pygame.Color('white'), ball.center, ball_radius)

    # Move the ball
    ball.x += ball_speed * dx
    ball.y += ball_speed * dy

   
    if ball.bottom > HEIGHT:
        print(game_score)
        print('GAME OVER')
        exit()
    elif not len(block_list):
        print(game_score)
        print("WIN!!!!!!!!!!!!!!!!!!!!!!!!!")
        exit()

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddle_speed
    if key[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.right += paddle_speed

    #  увеличение скорости шара на 30сек
    if pygame.time.get_ticks() % 30000 == 0:
        increase_ball_speed()

    # уменьшение весла каждые 45 сек
    if pygame.time.get_ticks() % 45000 == 0:
        shrink_paddle()

    pygame.display.flip()
    clock.tick(FPS)
