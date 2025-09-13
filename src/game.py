import pygame
from snake import Snake
from food import Food

class Game:
    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.reset()

    def reset(self):
        start_x = (self.width // (2 * self.cell_size)) * self.cell_size
        start_y = (self.height // (2 * self.cell_size)) * self.cell_size
        self.snake = Snake(self.cell_size, [start_x, start_y])
        self.food = Food(self.cell_size, self.width, self.height)
        self.score = 0
        self.game_over = False

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_UP, pygame.K_w):
                self.snake.change_direction("UP")
            elif event.key in (pygame.K_DOWN, pygame.K_s):
                self.snake.change_direction("DOWN")
            elif event.key in (pygame.K_LEFT, pygame.K_a):
                self.snake.change_direction("LEFT")
            elif event.key in (pygame.K_RIGHT, pygame.K_d):
                self.snake.change_direction("RIGHT")

    def update(self):
        if self.game_over:
            return

        self.snake.move()

        if self.snake.segments[0] == self.food.position:
            self.snake.grow()
            self.food.position = self.food.random_position()
            self.score += 1

        head = self.snake.segments[0]
        if (head[0] < 0 or head[0] >= self.width or
            head[1] < 0 or head[1] >= self.height):
            self.game_over = True

        if head in self.snake.segments[1:]:
            self.game_over = True

    def draw(self, surface):
        self.snake.draw(surface)
        self.food.draw(surface)
