import sys

import pygame

from globals import *


class Splash:
    def __init__(self, game):
        self.game = game
        pygame.display.set_caption("mazepy-3D")
        self.background = pygame.image.load("resources/textures/maze-title.png")
        font_18 = pygame.font.SysFont("FreeSans", 18)
        msg = f"Version:  {VERSION}"
        self.version = font_18.render(msg, True, (128, 128, 128))
        self.running = True

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                self.running = False

    def draw(self):
        self.game.screen.blit(self.background, (0, 0))
        x = HALF_WIDTH - self.version.get_width() // 2
        self.game.screen.blit(self.version, (x, HEIGHT - 50))
        pygame.display.flip()

    def run(self):
        self.draw()
        while self.running:
            self.check_events()
