import pygame
import noise
import numpy as np

pygame.init()

screen_width, screen_height = 800, 600
grid_size = 10

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Симплексный шум")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    shape = (screen_height // grid_size, screen_width // grid_size)
    scale = 0.1
    world = np.zeros(shape)
    
    for y in range(shape[0]):
        for x in range(shape[1]):
            value = noise.snoise2(x * scale, y * scale, octaves=6, persistence=0.5, lacunarity=2.0, repeatx=1024, repeaty=1024, base=0)
            color = int((value + 1) * 128)  # Преобразование значения в градацию серого
            pygame.draw.rect(screen, (color, color, color), (x * grid_size, y * grid_size, grid_size, grid_size))

    pygame.display.flip()

pygame.quit()
