import pygame

from globals import *


def load_map_data():
    data = []
    line_data = []
    with open(MAP_DATA_FILENAME, "r") as f:
        for line in f.readlines():
            line_data.append(line)
    for line in line_data:
        single_map = {}
        split_line = line.split(";")
        start = split_line[1].split(",")
        single_map["start"] = float(start[0]), float(start[1])
        single_map["angle"] = float(split_line[2])
        color = split_line[3].split(",")
        single_map["floor"] = int(color[0]), int(color[1]), int(color[2])
        single_map["sky"] = split_line[4]
        single_map["music"] = split_line[5]
        raw_map = split_line[6]
        mini_map = []
        for raw_row in raw_map.split("|"):
            row = []
            for cell in raw_row.split(","):
                row.append(int(cell))
            mini_map.append(row)
        single_map["mini_map"] = mini_map
        data.append(single_map)
    return data


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
        self.map_data = load_map_data()
        self.number_of_maps = len(self.map_data) + 1

    def get_map(self, number):
        self.world_map = {}
        single_map = self.map_data[number]
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
