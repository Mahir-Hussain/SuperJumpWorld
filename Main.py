import os
from sys import exit

import pygame
from pygame.locals import *

from services.level.levels import Level
from services.level.settings import *
from services.visualisation_service import visualizationService


class SuperJumpWorld:
    def __init__(self):
        self.width = 700
        self.height = 400
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.velocity = 3
        self.game = False
        self.start = False
        self.characterRect = visualizationService.get_lemon_character().get_rect()
        self.skyRect = visualizationService.get_world1("sky").get_rect()

    def initialize(self):
        clock = pygame.time.Clock()
        while True:
            pygame.display.set_caption("Super Jump World")
            pygame.display.set_icon(visualizationService.get_icon())

            keys = pygame.key.get_pressed()
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            self.startup(keys)

            if self.game == True:
                self.playerMovement(keys, self.characterRect)
                # self.worldMovement(self.skyRect)

                self.screenUpdater(
                    visualizationService.get_lemon_character(),
                    self.characterRect,
                    self.skyRect,
                )

    def startup(self, keyPressed):
        if self.start == False:
            startImg = visualizationService.get_startup()
            pygame.transform.scale(startImg, (self.width, self.height))
            rect = startImg.get_rect()

            self.screen.blit(startImg, rect)
            pygame.display.update()

        if keyPressed[pygame.K_p]:
            menuImg = visualizationService.get_menu()
            pygame.transform.scale(menuImg, (self.width, self.height))
            rect = menuImg.get_rect()

            self.screen.fill((0, 0, 0))
            self.screen.blit(menuImg, rect)
            pygame.display.update()
            self.start = True

        if self.start and keyPressed[pygame.K_1]:
            self.game = True

    def screenUpdater(self, character, characterRect, skyRect):
        self.screen.fill((200, 255, 255))

        # groundImg = visualizationService.get_world1("ground")
        # groundRect = groundImg.get_rect()

        skyImg = visualizationService.get_world1("sky")
        pyramids = visualizationService.get_world1("pyramids")

        self.screen.blit(skyImg, (skyRect.x, skyRect.y))
        self.screen.blit(pyramids, pyramids.get_rect())
        # self.screen.blit(groundImg, groundRect)
        level = Level(level_map1, self.screen)
        level.run()
        self.screen.blit(character, (characterRect.x, characterRect.y))

        pygame.display.update()

    # def worldMovement(self, skyRect):
    #     skyRect.x -= 1

    def playerMovement(
        self, keyPressed, rect
    ):  # Takes the users inputs to move the player
        if keyPressed[pygame.K_a] and rect.x - self.velocity > 0:
            rect.x -= self.velocity
        elif keyPressed[pygame.K_d]:
            rect.x += self.velocity
        if keyPressed[pygame.K_w]:
            rect.y -= self.velocity
        elif keyPressed[pygame.K_s]:
            rect.y += self.velocity


if __name__ == "__main__":
    SuperJumpWorld().initialize()
