import sys

import pygame

from globals import *


class MapSelectMenu:
    def __init__(self, game):
        self.game = game
        pygame.display.set_caption("mazepy-3D")
        self.background = pygame.image.load("resources/textures/maze.png")
        self.running = True
        font_80 = pygame.font.SysFont("FreeSans", 80, bold=True)
        self.font_30 = pygame.font.SysFont("FreeSans", 30)
        self.title = font_80.render("Select a Map", True, (30, 30, 30))
        self.number_of_buttons = self.game.map.number_of_maps
        self.button_list = self.setup_buttons()
        self.button_pressed = 0

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for i, button in enumerate(self.button_list):
                    if button.collidepoint(mouse_x, mouse_y):
                        self.button_pressed = i
                        self.running = False

    def draw(self):
        self.game.screen.blit(self.background, (0, 0))
        x = HALF_WIDTH - self.title.get_width() // 2
        self.game.screen.blit(self.title, (x, 50))
        self.display_buttons()
        pygame.display.flip()

    def display_buttons(self):
        for i, button in enumerate(self.button_list):
            pygame.draw.rect(self.game.screen, (200, 200, 200), button)
            num = self.font_30.render(f"{i + 1}", True, (0, 0, 0))
            x, y = button.center
            x = x - num.get_width() // 2
            y = y - num.get_height() // 2
            self.game.screen.blit(num, (x, y))

    def setup_buttons(self):
        button_list = []
        x = 210
        y = 150
        for i in range(1, self.number_of_buttons + 1):
            button_list.append(pygame.rect.Rect((x, y, 100, 100)))
            if i % 10 == 0:
                x = 210
                y += 200
            else:
                x += 120
        return button_list

    def run(self):
        self.draw()
        while self.running:
            self.check_events()
        return self.button_pressed
