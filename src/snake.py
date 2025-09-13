import pygame

class Snake:
    def __init__(self, cell_size, start_pos):
        self.cell_size = cell_size
        self.segments = [
            (start_pos[0], start_pos[1]),
            (start_pos[0] - cell_size, start_pos[1]),
            (start_pos[0] - 2 * cell_size, start_pos[1])
        ]
        self.direction = "RIGHT"

    def move(self):
        head_x, head_y = self.segments[0]
        if self.direction == "UP":
            new_head = (head_x, head_y - self.cell_size)
        elif self.direction == "DOWN":
            new_head = (head_x, head_y + self.cell_size)
        elif self.direction == "LEFT":
            new_head = (head_x - self.cell_size, head_y)
        elif self.direction == "RIGHT":
            new_head = (head_x + self.cell_size, head_y)
        self.segments = [new_head] + self.segments[:-1]

    def grow(self):
        self.segments.append(self.segments[-1])

    def change_direction(self, new_dir):
        opposite = {"UP":"DOWN","DOWN":"UP","LEFT":"RIGHT","RIGHT":"LEFT"}
        if new_dir != opposite[self.direction]:
            self.direction = new_dir

    def draw(self, surface):
        for x, y in self.segments:
            rect = pygame.Rect(x, y, self.cell_size, self.cell_size)
            pygame.draw.rect(surface, (0, 200, 0), rect)
