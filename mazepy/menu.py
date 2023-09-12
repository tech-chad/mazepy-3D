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
        self.number_of_pages = self.number_of_buttons // 50
        self.page = 0
        self.button_list = self.setup_buttons()
        self.button_pressed = 0
        self.next_button = pygame.rect.Rect((WIDTH - 500, 750, 200, 100))
        self.next_text = self.font_30.render("NEXT", True, (30, 30, 30))
        self.previous_button = pygame.rect.Rect((300, 750, 200, 100))
        self.previous_text = self.font_30.render("PREVIOUS", True, (30, 30, 30))

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
                        self.button_pressed = i + self.page * 50
                        self.running = False
                        return None
                if self.next_button.collidepoint(mouse_x, mouse_y):
                    if self.page < self.number_of_pages:
                        self.page += 1
                        return None
                if self.previous_button.collidepoint(mouse_x, mouse_y):
                    if self.page > 0:
                        self.page -= 1
                        return None
            if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                self.game.sound.toggle_mute()

    def draw(self):
        self.game.screen.blit(self.background, (0, 0))
        x = HALF_WIDTH - self.title.get_width() // 2
        self.game.screen.blit(self.title, (x, 50))
        self.display_buttons()
        pygame.display.flip()

    def display_buttons(self):
        start = 0 + self.page * 50
        for i, button in enumerate(self.button_list[start:]):
            if i + 1 == 51:
                break
            pygame.draw.rect(self.game.screen, (200, 200, 200), button)
            n = (i + 1) + self.page * 50
            num = self.font_30.render(f"{n}", True, (0, 0, 0))
            x, y = button.center
            x = x - num.get_width() // 2
            y = y - num.get_height() // 2
            self.game.screen.blit(num, (x, y))
        pygame.draw.rect(self.game.screen, (110, 110, 110), self.next_button)
        x, y = self.next_button.center
        x = x - self.next_text.get_width() // 2
        y = y - self.next_text.get_height() // 2
        self.game.screen.blit(self.next_text, (x, y))
        pygame.draw.rect(self.game.screen, (110, 110, 110), self.previous_button)
        x, y = self.previous_button.center
        x = x - self.previous_text.get_width() // 2
        y = y - self.previous_text.get_height() // 2
        self.game.screen.blit(self.previous_text, (x, y))

    def setup_buttons(self):
        button_list = []
        x = 210
        y = 150

        for i in range(1, self.number_of_buttons):
            button_list.append(pygame.rect.Rect((x, y, 100, 100)))
            if i % 50 == 0:
                x = 210
                y = 150
            elif i % 10 == 0:
                x = 210
                y += 120
            else:
                x += 120
        return button_list

    def run(self):
        self.game.sound.play_theme_music()
        self.running = True
        self.button_pressed = 0
        pygame.mouse.set_visible(True)
        while self.running:
            self.draw()
            self.check_events()
        return self.button_pressed


class Completed:
    def __init__(self, game):
        self.game = game
        self.running = True
        self.background = pygame.image.load("resources/textures/maze.png")
        font_120 = pygame.font.SysFont("FreeSans", 120, bold=True)
        font_30 = pygame.font.SysFont("FreeSans", 30)
        self.title1 = font_120.render("Maze Completed!", True, (255, 30, 255))
        self.title2 = font_120.render("Excellent!", True, (255, 30, 255))
        self.msg = font_30.render("Press any key to continue", True, (240, 240, 240))

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.running = False

    def draw(self):
        self.game.screen.blit(self.background, (0, 0))
        x = HALF_WIDTH - self.title1.get_width() // 2
        self.game.screen.blit(self.title1, (x, 100))
        x = HALF_WIDTH - self.title2.get_width() // 2
        self.game.screen.blit(self.title2, (x, 300))
        x = HALF_WIDTH - self.msg.get_width() // 2
        self.game.screen.blit(self.msg, (x, HEIGHT - 100))
        pygame.display.flip()

    def run(self):
        self.game.sound.play_winner_music()
        self.running = True
        pygame.mouse.set_visible(True)
        self.draw()
        while self.running:
            self.check_events()


class ConfirmBox:
    def __init__(self, game, msg, true_msg="Yes", false_msg="No"):
        self.game = game
        font_50 = pygame.font.SysFont("FreeSans", 50)
        box_width = 500
        box_height = 300
        x = HALF_WIDTH - box_width // 2
        y = HALF_HEIGHT - box_height // 2
        self.msg_box = pygame.rect.Rect(x, y, box_width, box_height)
        x = self.msg_box.left + 50
        y = self.msg_box.bottom - 150
        self.true_box = pygame.rect.Rect(x, y, 150, 100)
        x = self.msg_box.right - 200
        y = self.msg_box.bottom - 150
        self.false_box = pygame.rect.Rect(x, y, 150, 100)
        self.message = font_50.render(msg, True, (0, 0, 0))
        self.true_msg = font_50.render(true_msg, True, (0, 0, 0))
        self.false_msg = font_50.render(false_msg, True, (0, 0, 0))
        self.running = True
        self.result = False

    def check_for_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False
                self.result = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if self.true_box.collidepoint(mouse_x, mouse_y):
                    self.running = False
                    self.result = True
                elif self.false_box.collidepoint(mouse_x, mouse_y):
                    self.running = False
                    self.result = False

    def draw(self):
        pygame.draw.rect(self.game.screen, (130, 130, 130), self.msg_box)
        pygame.draw.rect(self.game.screen, (210, 210, 210), self.true_box)
        pygame.draw.rect(self.game.screen, (210, 210, 210), self.false_box)
        x = HALF_WIDTH - self.message.get_width() // 2
        self.game.screen.blit(self.message, (x, HALF_HEIGHT - 100))
        x = self.true_box.centerx - self.true_msg.get_width() // 2
        y = self.true_box.centery - self.true_msg.get_height() // 2
        self.game.screen.blit(self.true_msg, (x, y))
        x = self.false_box.centerx - self.false_msg.get_width() // 2
        y = self.false_box.centery - self.false_msg.get_height() // 2
        self.game.screen.blit(self.false_msg, (x, y))
        pygame.display.flip()

    def run(self):
        self.running = True
        pygame.mouse.set_visible(True)
        self.draw()
        while self.running:
            self.check_for_events()
        pygame.mouse.set_visible(False)
        return self.result
