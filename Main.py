from sys import exit

import pygame
from pygame.locals import *

from level.levels import Level
from level.settings import *
from services.player import Player
from services.sound_service import soundService
from services.visualisation_service import visualizationService

## TODO
## Add enemy sprites + logic
## Add an actual level
## Death screen - go back to the level
## Enemies
## Time
## Sound
## Add the sky moving - possible function
## Reflect changes in documentation
##


class SuperJumpWorld:  # Main class
    def __init__(self):
        self.screen = pygame.display.set_mode((screenWidth, screenHeight))
        # Initialize
        self.game = False
        self.start = False
        self.level = Level(levelMap, self.screen)

    def initialize(self):  # Opens the pygame window
        pygame.init()
        soundService.get_background()
        clock = pygame.time.Clock()
        # World images
        skyImg = visualizationService.get_world1("sky")
        pyramids = visualizationService.get_world1("pyramids")
        # skyRect = visualizationService.get_world1("sky").get_rect()
        while True:
            # Setting the pygame window up
            pygame.display.set_caption("Super Jump World")
            pygame.display.set_icon(visualizationService.get_icon())

            keys = pygame.key.get_pressed()  # To get user input

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            self.startup(keys)

            if self.game == True:
                self.screenUpdater(skyImg, pyramids)
            if keys[pygame.K_0]:
                SuperJumpWorld().initialize()

            clock.tick(30)  # FPS at 30

    def startup(self, keyPressed):  # Displays the startup and menu screen.
        self.screen.fill((0, 0, 0))  # Creates a blank window to be drawn on
        if self.start == False:  # Goes to startup screen
            # Images
            startImg = visualizationService.get_startup()
            rect = startImg.get_rect()
            # Drawing
            self.screen.blit(startImg, rect)
            pygame.display.update()

        if keyPressed[pygame.K_p] and self.game == False:  # Goes to menu
            # Images
            menuImg = visualizationService.get_menu()
            rect = menuImg.get_rect()
            # Drawing
            self.screen.blit(menuImg, rect)
            pygame.display.update()

            self.start = True

        if self.start:
            self.menu(keyPressed)

    def menu(self, keyPressed):
        if keyPressed[pygame.K_1]:  # Goes to main game
            self.game = True
        elif keyPressed[pygame.K_2]:  # Goes to leaderboard
            pass
        elif keyPressed[pygame.K_3]:  # Goes to settings
            pass
        elif keyPressed[pygame.K_4]:  # Exits the game
            exit()

    def screenUpdater(self, skyImg, pyramids):
        self.screen.fill((0, 0, 0))  # Creates a blank window to be drawn on
        # World drawing
        # self.screen.blit(skyImg, (skyRect.x, skyRect.y))
        self.screen.blit(skyImg, skyImg.get_rect())
        self.screen.blit(pyramids, pyramids.get_rect())
        # level drawing
        self.level.run()  # Runs the level.run() command found in level/levels.py
        pygame.display.update()


if __name__ == "__main__":
    SuperJumpWorld().initialize()
