import pygame

import map_data


class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = None
        self.player_start = None
        self.player_start_angle = None
        self.sky = None
        self.floor_type = None
        self.floor = None
        self.music = None
        self.world_map = {}
        self.number_of_maps = len(map_data.maps) + 1
        # self.get_map()

    def get_map(self, number):
        self.world_map = {}
        single_map = map_data.maps[number]
        self.mini_map = single_map["mini_map"]
        self.player_start = single_map["start"]
        self.player_start_angle = single_map["angle"]
        self.sky = single_map["sky"]
        self.floor = single_map["floor"]
        self.music = single_map["music"]
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

    def draw(self):
        [pygame.draw.rect(self.game.screen, "darkgray",
                          (pos[0] * 100, pos[1] * 100, 100, 100), 2)
         for pos in self.world_map]
