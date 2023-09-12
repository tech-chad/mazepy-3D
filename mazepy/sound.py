
import pygame


class Sound:
    def __init__(self):
        pygame.mixer.init()
        path = "resources/sound/"
        self.theme = pygame.mixer.Sound(path + "theme.mp3")
        self.theme.set_volume(0.3)
        self.winner_theme = pygame.mixer.Sound(path + "winning.mp3")
        self.winner_theme.set_volume(0.3)
        self.level_music = {}
        for x in range(4):
            t = pygame.mixer.Sound(path + f"Level{x}.mp3")
            t.set_volume(0.2)
            self.level_music[x] = t
        self.currently_playing = None
        self.mute = False

    def play_level_music(self, level: int):
        if self.currently_playing is not None and pygame.mixer.get_busy():
            self.currently_playing.fadeout(1000)
        self.currently_playing = self.level_music[level]
        if not self.mute:
            self.currently_playing.play(-1)

    def play_winner_music(self):
        if self.currently_playing is not None and pygame.mixer.get_busy():
            self.currently_playing.fadeout(1000)
        self.currently_playing = self.winner_theme
        if not self.mute:
            self.currently_playing.play()

    def play_theme_music(self):
        if self.currently_playing == self.theme:
            return
        if self.currently_playing is not None and pygame.mixer.get_busy():
            self.currently_playing.fadeout(1000)
        self.currently_playing = self.theme
        if not self.mute:
            self.currently_playing.play(-1)

    def stop(self):
        if self.currently_playing is not None and pygame.mixer.get_busy():
            self.currently_playing.fadeout(1000)
        self.currently_playing = None

    def toggle_mute(self):
        if self.mute:
            self.mute = False
            self.currently_playing.play(-1)
        else:
            self.currently_playing.stop()
            self.mute = True
