import pygame
import random

class Food:
    def __init__(self, cell_size, width, height):
        self.cell_size = cell_size
        self.width = width
        self.height = height
        self.position = (0, 0)

    def random_position(self, snake_body, walls):
        while True:
            x = random.randrange(0, self.width, self.cell_size)
            y = random.randrange(0, self.height, self.cell_size)
            pos = (x, y)
            if pos not in snake_body and pos not in walls:
                return pos

    def draw(self, surface):
        rect = pygame.Rect(self.position[0], self.position[1], self.cell_size, self.cell_size)
        pygame.draw.rect(surface, (200, 0, 0), rect)
