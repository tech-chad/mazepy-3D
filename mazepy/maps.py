import pygame

_ = False
map1 = {
    "mini_map": [
        [1, 8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, _, 1, _, _, _, 1, _, _, _, _, _, 1, _, _, 1],
        [1, _, 1, _, 1, 1, 1, _, 1, _, 1, _, _, _, 1, 1],
        [1, _, 1, _, _, _, _, _, 1, 1, 1, 1, 1, _, 1, 1],
        [1, _, 1, _, 1, _, 1, _, 1, _, _, _, 1, _, _, 1],
        [1, _, _, _, 1, _, 1, _, _, _, 1, _, 1, 1, _, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9, 1],
    ],
    "start": (1.5, 1.5),
    "angle": 1.5

}


class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = map1["mini_map"]
        self.player_start = map1["start"]
        self.player_start_angle = map1["angle"]
        self.world_map = {}
        self.get_map()

    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

    def draw(self):
        [pygame.draw.rect(self.game.screen, "darkgray",
                          (pos[0] * 100, pos[1] * 100, 100, 100), 2)
         for pos in self.world_map]
