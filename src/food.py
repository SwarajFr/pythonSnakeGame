import pygame, random

class Food:
    def __init__(self, cell_size, width, height):
        self.cell_size = cell_size
        self.width = width
        self.height = height
        self.position = self.random_position()

    def random_position(self):
        x = random.randint(0, (self.width - self.cell_size) // self.cell_size) * self.cell_size
        y = random.randint(0, (self.height - self.cell_size) // self.cell_size) * self.cell_size
        return [x, y]

    def draw(self, surface):
        pygame.draw.rect(surface, (200, 0, 0), (*self.position, self.cell_size, self.cell_size))
