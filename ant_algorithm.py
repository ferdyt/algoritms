import pygame
import numpy as np

pygame.init()

width, height = 1280, 720
cell_size = 10

screen = pygame.display.set_mode((width, height))

white = (255, 255, 255)
black = (0, 0, 0)

# Инициализация массива для решетки (0 - белая клетка, 1 - черная клетка)
grid = np.zeros((width // cell_size, height // cell_size), dtype=int)

# Положение муравья и его направление
ant_pos = [grid.shape[0] // 2, grid.shape[1] // 2]
ant_direction = 0  # Направление: 0 - вверх, 1 - вправо, 2 - вниз, 3 - влево

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Чтение состояния текущей клетки
    current_cell = grid[ant_pos[0], ant_pos[1]]

    # Поворот муравья в зависимости от состояния клетки
    if current_cell == 0:
        ant_direction = (ant_direction + 1) % 4
    else:
        ant_direction = (ant_direction - 1) % 4

    # Инвертирование цвета текущей клетки
    grid[ant_pos[0], ant_pos[1]] = 1 - current_cell

    # Перемещение муравья
    if ant_direction == 0:
        ant_pos[1] = (ant_pos[1] - 1) % grid.shape[1]
    elif ant_direction == 1:
        ant_pos[0] = (ant_pos[0] + 1) % grid.shape[0]
    elif ant_direction == 2:
        ant_pos[1] = (ant_pos[1] + 1) % grid.shape[1]
    elif ant_direction == 3:
        ant_pos[0] = (ant_pos[0] - 1) % grid.shape[0]

    # Отрисовка решетки
    screen.fill(white)
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == 1:
                pygame.draw.rect(screen, black, (i * cell_size, j * cell_size, cell_size, cell_size))

    pygame.display.flip()

pygame.quit()
