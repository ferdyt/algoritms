import pygame
import random
import time

pygame.init()

screen_width, screen_height = 1280, 720

grid_size = 10

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

iteration = 100
count = 0

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Генерация пещер")

# Функция для создания случайного направления
def get_random_direction():
    return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])

# Создаем сетку
grid = [[random.choice([True, False]) for _ in range(grid_width)] for _ in range(grid_height)]

running = True
time.sleep(5)
while running:
    time.sleep(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Выбираем случайное место для начала дрифта
    x, y = random.randint(0, len(grid[0]) - 1), random.randint(0, len(cave_grid) - 1)
    
    # Дрифт
    if count <= iteration:
        for _ in range(500):
            grid[y][x] = True
            dx, dy = get_random_direction()
            x = max(0, min(x + dx, len(grid[0]) - 1))
            y = max(0, min(y + dy, len(grid) - 1))

    screen.fill(YELLOW)

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x]:
                pygame.draw.rect(screen, BLACK, (x * grid_size, y * grid_size, grid_size, grid_size))

    pygame.display.flip()

    count += 1

# Выход из игры
pygame.quit()
