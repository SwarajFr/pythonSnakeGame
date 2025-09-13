import pygame

class UI:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.font = pygame.font.SysFont("Arial", 30)
        self.big_font = pygame.font.SysFont("Arial", 60, bold=True)

    def draw_score(self, surface, score):
        text = self.font.render(f"Score: {score}", True, (255, 255, 255))
        surface.blit(text, (10, 10))

    def draw_game_over(self, surface, score, replay_button, quit_button=None):
        text = self.big_font.render("GAME OVER", True, (200, 0, 0))
        score_text = self.font.render(f"Final Score: {score}", True, (255, 255, 255))

        surface.blit(text, (self.width//2 - text.get_width()//2, self.height//2 - 120))
        surface.blit(score_text, (self.width//2 - score_text.get_width()//2, self.height//2 - 60))

        replay_button.draw(surface)
        if quit_button:
            quit_button.draw(surface)

    def draw_start_menu(self, surface):
        text = self.big_font.render("Press ENTER to Start", True, (0, 200, 0))
        surface.blit(text, (self.width//2 - text.get_width()//2, self.height//2))


class Button:
    def __init__(self, x, y, width, height, text, font, bg_color=(0,150,0), text_color=(255,255,255)):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = font
        self.bg_color = bg_color
        self.text_color = text_color

    def draw(self, surface):
        pygame.draw.rect(surface, self.bg_color, self.rect, border_radius=12)
        text_surf = self.font.render(self.text, True, self.text_color)
        surface.blit(
            text_surf,
            (self.rect.x + (self.rect.width - text_surf.get_width()) // 2,
             self.rect.y + (self.rect.height - text_surf.get_height()) // 2)
        )

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
