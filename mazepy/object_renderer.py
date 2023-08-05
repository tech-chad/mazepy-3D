import pygame

from globals import *


class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()
        # self.sky_image = self.get_texture("resources/textures/sky.png",
        #                                   (WIDTH, HALF_HEIGHT))
        image_path = f"resources/textures/{self.game.map.sky}"
        self.celling_image = self.get_texture(image_path,
                                              (WIDTH, HALF_HEIGHT))
        self.floor_color = self.game.map.floor
        # self.background_image1 = self.get_texture("resources/textures/background1.png",
        # (WIDTH, HALF_HEIGHT))
        self.sky_offset = 0
        self.celling_image_offset = 0
        self.background_image1_offset = 0

    def draw(self):
        self.draw_background()
        self.render_game_objects()

    def draw_background(self):
        # self.screen.fill("yellow")
        # self.sky_offset = (self.sky_offset + 4.5 * self.game.player.rel) % settings.WIDTH
        # self.screen.blit(self.sky_image, (-self.sky_offset, 0))
        # self.screen.blit(self.sky_image, (-self.sky_offset + settings.WIDTH, 0))
        self.celling_image_offset = (self.celling_image_offset + 4.5 *
                                     self.game.player.rel) % WIDTH
        self.screen.blit(self.celling_image, (-self.celling_image_offset, 0))
        self.screen.blit(self.celling_image, (-self.celling_image_offset +
                                              WIDTH, 0))
        # self.background_image1_offset = (self.background_image1_offset +
        #                                  4.5 * self.game.player.rel) % settings.WIDTH
        # self.screen.blit(self.background_image1, (-self.background_image1_offset, 0))
        # self.screen.blit(self.background_image1, (-self.background_image1_offset +
        #                                           settings.WIDTH, 0))
        # floor
        pygame.draw.rect(self.screen, self.floor_color, (0, HALF_HEIGHT, WIDTH, HEIGHT))

    def render_game_objects(self):
        list_objects = sorted(self.game.raycasting.objects_to_render,
                              key=lambda t: t[0], reverse=True)
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)

    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(texture, res)

    def load_wall_textures(self):
        return {
            1: self.get_texture("resources/textures/1.png"),
            2: self.get_texture("resources/textures/2.png"),
            3: self.get_texture("resources/textures/3.png"),
            # 4: self.get_texture("resources/textures/4.png"),
            # 5: self.get_texture("resources/textures/5.png"),
            # 7: self.get_texture("resources/textures/7.png"),
            8: self.get_texture("resources/textures/8.png"),
            9: self.get_texture("resources/textures/9.png"),
        }
