import pygame

class Snake:
    def __init__(self, cell_size, start_pos):
        self.cell_size = cell_size
        self.segments = [
            start_pos[:],
            [start_pos[0] - cell_size, start_pos[1]],
            [start_pos[0] - 2 * cell_size, start_pos[1]]
        ]
        self.direction = "RIGHT"

    def move(self):
        head = self.segments[0][:]
        if self.direction == "UP":
            head[1] -= self.cell_size
        elif self.direction == "DOWN":
            head[1] += self.cell_size
        elif self.direction == "LEFT":
            head[0] -= self.cell_size
        elif self.direction == "RIGHT":
            head[0] += self.cell_size

        self.segments.insert(0, head)
        self.segments.pop()

    def grow(self):
        self.segments.append(self.segments[-1][:])

    def change_direction(self, new_dir):
        opposite = {"UP":"DOWN","DOWN":"UP","LEFT":"RIGHT","RIGHT":"LEFT"}
        if new_dir != opposite[self.direction]:
            self.direction = new_dir

    def draw(self, surface):
        for seg in self.segments:
            pygame.draw.rect(surface, (0, 200, 0), (*seg, self.cell_size, self.cell_size))
