import pygame
import random
import numpy as np
import time

# Инициализация Pygame
pygame.init()

# Размеры экрана
screen_width, screen_height = 1280, 720

# Размер сетки
grid_size = 10

ore_chance = 1

# Размеры сетки на экране
grid_width = screen_width // grid_size
grid_height = screen_height // grid_size

# Цвета
BLACK = (50, 50, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 200, 200)

update_count = 10

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Karva's algorithm")

# Инициализация сетки
grid = [[random.choice([True, False]) for _ in range(grid_width)] for _ in range(grid_height)]

# Функция для обновления состояния клеток сетки
def update_cave_grid(grid):
    new_grid = [[False for _ in range(grid_width)] for _ in range(grid_height)]
    for y in range(1, grid_height - 1):
        for x in range(1, grid_width - 1):
            wall_count = sum(1 for i in range(-1, 2) for j in range(-1, 2) if cave_grid[y + i][x + j])
            if wall_count >= 5:
                new_grid[y][x] = 1

            if new_grid[y][x] == 1 and random.randint(1, 100) <= ore_chance:
                new_grid[y][x] = 2

    return new_grid

# Основной цикл
def screen_update(grid):
    count = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Обновление состояния сетки
        if count <= update_count:
            print(f"update epoch {count} / {update_count}")
            grid = update_cave_grid(grid)
            count += 1
        else:
            break

        # Очистка экрана
        screen.fill(BLACK)

        # Отрисовка сетки пещер
        for y in range(grid_height):
            for x in range(grid_width):
                if grid[y][x] == 1:
                    pygame.draw.rect(screen, YELLOW, (x * grid_size, y * grid_size, grid_size, grid_size))

                elif grid[y][x] == 2:
                    pygame.draw.rect(screen, CYAN, (x * grid_size, y * grid_size, grid_size, grid_size))


        pygame.display.flip()

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        grid = [[random.choice([True, False]) for _ in range(grid_width)] for _ in range(grid_height)]
        screen_update(grid)
        time.sleep(1)

    pygame.quit()

if __name__ == "__main__":
    main()
