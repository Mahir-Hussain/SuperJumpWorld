import random
from sys import exit

import pygame
from pygame.locals import *

import level.settings as settings
from level.levels import Level
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
        self.screen = pygame.display.set_mode(
            (settings.screenWidth, settings.screenHeight)
        )
        # Initialize
        self.game = False
        self.start = False
        self.worldChoice = random.randint(1, 3)
        self.level = Level(self.screen)

    def worldChooser(self):
        if self.worldChoice == 1:
            skyImg = visualizationService.get_world1("sky")
            pyramids = visualizationService.get_world1("pyramids")
            return skyImg, pyramids
        elif self.worldChoice == 2:
            skyImg = visualizationService.get_world2("sky")
            background = visualizationService.get_world2("background")
            return skyImg, background
        elif self.worldChoice == 3:
            skyImg = visualizationService.get_world3("sky")
            background = visualizationService.get_world3("background")
            return skyImg, background

    def initialize(self):
        """
        Opens the pygame window.
        Runs throughout the duration of the game being
        opened.
        Runs different functions depending on variable boolean states
        """
        pygame.init()
        clock = pygame.time.Clock()
        # World images
        skyImg, background = self.worldChooser()
        # skyRect = visualizationService.get_world1("sky").get_rect()
        while True:
            # Setting the pygame window up
            pygame.display.set_caption("Super Jump World")
            pygame.display.set_icon(visualizationService.get_icon())

            self.keys = pygame.key.get_pressed()  # To get user input

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            self.startup(self.keys)

            if self.game == True:
                self.screenUpdater(skyImg, background)

            clock.tick(30)  # FPS at 30

    def startup(self, keyPressed):
        """
        Displays the startup and menu screen.
        """
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
            self.menu()

    def menu(self):
        """
        Changes variable names which change the
        outcome of the initialize function
        """
        if self.keys[pygame.K_1]:  # Goes to main game
            self.game = True
        elif self.keys[pygame.K_2]:  # Goes to leaderboard
            pass
        elif self.keys[pygame.K_3]:  # Goes to settings
            pass
        elif self.keys[pygame.K_4]:  # Exits the game
            exit()

    def screenUpdater(self, skyImg, background):
        """
        When the game is lauchned, this function is launched.
        If player is not dead, run the game
        If dead, show death screen
        Game can be restarted if dead
        """
        self.screen.fill((0, 0, 0))  # Creates a blank window to be drawn on
        if settings.death == False:
            # World drawing
            # self.screen.blit(skyImg, (skyRect.x, skyRect.y))
            self.screen.blit(skyImg, skyImg.get_rect())
            self.screen.blit(background, background.get_rect())
            # level drawing
            self.level.run()  # Runs the level.run() command found in level/levels.py
        elif settings.death == True:
            self.onDeath()
        pygame.display.update()

    def onDeath(self):
        """
        When the player is dead,
        this function handles what happens after
        """
        # Images
        gameOver = visualizationService.get_gameOver()
        # Drawing
        self.screen.blit(gameOver, gameOver.get_rect())
        # Restart game
        if self.keys[pygame.K_c]:
            settings.death = False
            self.game = False
            self.level = Level(self.screen)
            SuperJumpWorld().startup(self.keys)


if __name__ == "__main__":
    SuperJumpWorld().initialize()
