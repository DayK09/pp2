import pygame
import sys
from pygame.locals import *
import random
import time

# Инициализация
pygame.init()

# Настройка FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Определение цветов
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Остальные переменные для использования в программе
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 2
SCORE = 0

# Настройка шрифтов
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")
coin = pygame.image.load("coin.png")
n_enemy = pygame.image.load("truck.png")

# Создание белого экрана
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SPEED
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class NewEnemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("truck.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SPEED
        self.rect.move_ip(0, SPEED * 0.5)  # Уменьшаем скорость в 2 раза по сравнению с обычным врагом
        if self.rect.bottom > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")  # Загрузка изображения монеты
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SPEED
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


# Настройка спрайтов
P1 = Player()
E1 = Enemy()

# Создание групп спрайтов
enemies = pygame.sprite.Group()
enemies.add(E1)
new_enemies = pygame.sprite.Group()  # Группа для нового вида врагов
coins = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

# Добавление нового пользовательского события
SPAWN_COIN = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_COIN, 50000)  # Создаем новую монету каждые 5 секунд
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
# Игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.2
        if event.type == SPAWN_COIN:
            new_coin = Coin()
            coins.add(new_coin)
            all_sprites.add(new_coin)
        if SCORE >= 30 and len(new_enemies) == 0:  # Появление нового врага после набора 30 очков
            new_enemy = NewEnemy()
            new_enemies.add(new_enemy)
            all_sprites.add(new_enemy)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))

    for entity in all_sprites:
        if isinstance(entity, Enemy) or isinstance(entity, Player):
            entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    for coin in coins:
        coin.move()
        DISPLAYSURF.blit(coin.image, coin.rect)

    for new_enemy in new_enemies:  # Движение нового врага
        new_enemy.move()
        DISPLAYSURF.blit(new_enemy.image, new_enemy.rect)

    if pygame.sprite.spritecollideany(P1, enemies) or pygame.sprite.spritecollideany(P1, new_enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(1)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Проверка на столкновение между игроком и монетами
    collected_coins = pygame.sprite.spritecollide(P1, coins, True)
    for coin in collected_coins:
        SCORE += 1

    # Проверка на столкновение между обычным и новым врагом
    if pygame.sprite.groupcollide(enemies, new_enemies, False, False):
        for new_enemy in new_enemies:
            new_enemy.rect.y += 50  # Смещаем нового врага вниз

    pygame.display.update()
    FramePerSec.tick(FPS)
