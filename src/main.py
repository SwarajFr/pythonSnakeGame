import pygame, sys
from game import Game
from ui import UI, Button

pygame.init()
WIDTH, HEIGHT = 1280, 720
CELL_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game 🐍")

clock = pygame.time.Clock()
game = Game(WIDTH, HEIGHT, CELL_SIZE)
ui = UI(WIDTH, HEIGHT)

state = "MENU"  # (MENU, PLAYING, GAME_OVER)

replay_button = Button(WIDTH//2 - 100, HEIGHT//2, 200, 60, "Replay", ui.font)
quit_button = Button(WIDTH//2 - 100, HEIGHT//2 + 80, 200, 60, "Quit", ui.font, bg_color=(150,0,0))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if state == "MENU":
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                state = "PLAYING"
                game.reset()

        elif state == "PLAYING":
            game.handle_event(event)

        elif state == "GAME_OVER":
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                state = "MENU"
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if replay_button.is_clicked(event.pos):
                    game.reset()
                    state = "PLAYING"
                elif quit_button.is_clicked(event.pos):
                    running = False

    if state == "PLAYING":
        game.update()
        if game.game_over:
            state = "GAME_OVER"

    screen.fill((0, 0, 0))

    if state == "MENU":
        ui.draw_start_menu(screen)
    elif state == "PLAYING":
        game.draw(screen)
        ui.draw_score(screen, game.score)
    elif state == "GAME_OVER":
        ui.draw_game_over(screen, game.score, replay_button, quit_button)

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
sys.exit()
