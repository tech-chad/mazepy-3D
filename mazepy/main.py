import sys

import pygame

import maps
import menu
import object_renderer
import player
import raycasting
import sound
import splash

from globals import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        self.delta_time = 1
        self.map = maps.Map(self)
        self.player = None
        self.raycasting = None
        self.object_renderer = None
        self.splash_screen = splash.Splash(self)
        self.map_select = menu.MapSelectMenu(self)
        self.completed = menu.Completed(self)
        self.quit_confirm = menu.ConfirmBox(self, msg="Quit the map?")
        self.rest_confirm = menu.ConfirmBox(self, msg="Reset to start?")
        self.sound = sound.Sound()
        self.map_number = 0
        self.running = True

    def new_game(self, map_number):  # pass in map number
        self.map.get_map(map_number)
        self.player = player.Player(self)
        self.object_renderer = object_renderer.ObjectRenderer(self)
        self.raycasting = raycasting.RayCasting(self)

    def update(self):
        self.player.update()
        self.raycasting.update()
        pygame.display.flip()
        self.delta_time = self.clock.tick(FPS)
        caption = f"mazepy-3D    FPS: {self.clock.get_fps() :.1f}"
        pygame.display.set_caption(caption)

    def draw(self):
        self.object_renderer.draw()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                if self.quit_confirm.run():
                    self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                if self.quit_confirm.run():
                    self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                if self.rest_confirm.run():
                    self.new_game(self.map_number)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                self.sound.toggle_mute()

    def run(self):
        self.splash_screen.run()
        while True:
            self.running = True
            self.map_number = self.map_select.run()
            self.new_game(self.map_number)
            pygame.mouse.set_visible(False)
            self.sound.play_level_music(int(self.map.music))
            while self.running:
                self.check_events()
                self.update()
                self.draw()
            # self.sound.level_music[self.map.music].fadeout(1000)


def main():
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
