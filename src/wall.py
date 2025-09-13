import pygame

class WallManager:
    def __init__(self, cell_size, width, height):
        self.cell_size = cell_size
        self.width = width
        self.height = height
        self.walls = []

    def add_wall_in_front(self, snake_head, snake_direction, food_pos, snake_body=None):
        dx, dy = 0, 0
        if snake_direction == "UP":
            dy = -self.cell_size
        elif snake_direction == "DOWN":
            dy = self.cell_size
        elif snake_direction == "LEFT":
            dx = -self.cell_size
        elif snake_direction == "RIGHT":
            dx = self.cell_size
        pos = (snake_head[0] + dx * 3, snake_head[1] + dy * 3)
        if (0 <= pos[0] < self.width and 
            0 <= pos[1] < self.height and
            pos != food_pos and
            (snake_body is None or pos not in snake_body) and
            pos not in self.walls):
            self.walls.append(pos)

    def draw(self, surface):
        for wall in self.walls:
            rect = pygame.Rect(wall[0], wall[1], self.cell_size, self.cell_size)
            pygame.draw.rect(surface, (255, 255, 255), rect)
