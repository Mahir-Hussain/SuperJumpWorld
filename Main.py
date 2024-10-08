from random import randint
from sys import exit

import pygame
from pygame.locals import *

import level.settings as settings
from level.levels import Level
from services.sound_service import soundService
from services.visualisation_service import visualizationService


class SuperJumpWorld:  # Main class
    def __init__(self):
        self.screen = pygame.display.set_mode(
            (settings.screenWidth, settings.screenHeight)
        )
        # Initialize
        self.game = False
        self.start = False
        # Level
        self.worldChoice = randint(1, 3)
        self.level = Level(self.screen)
        self.deathTime = 0

    def worldChooser(self):
        """
        Runs a different background image each time the game is run
        """
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
        Runs throughout thez duration of the game being
        opened.
        Runs different functions depending on variable boolean states
        """
        pygame.init()
        clock = pygame.time.Clock()
        # World images
        skyImg, background = self.worldChooser()
        while True:
            soundService.get_background()
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

            clock.tick(30)  # FPS locked at 30

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
        When the game is launched, this function is launched.
        If player is not dead, run the game
        If dead, show death screen
        Game can be restarted if dead
        """
        self.screen.fill((0, 0, 0))  # Creates a blank window to be drawn on
        # Time variable
        self.time = pygame.time.get_ticks()
        time = round(self.time / 1000)

        if settings.finish:  # If player has finished the level
            self.onFinish()

        elif settings.death:  # If the player is dead
            soundService.get_death()
            self.onDeath()

        else:  # If not dead or finished, run the level
            # World drawing
            self.screen.blit(skyImg, skyImg.get_rect())
            self.screen.blit(background, background.get_rect())

            # Text drawing
            font = pygame.font.Font("freesansbold.ttf", 20)
            time = font.render(f"Time: {time - self.deathTime}", True, (255, 140, 0))
            score = font.render(f"Score: {settings.score}", True, (255, 140, 0))

            # level drawing
            self.level.run()  # Runs the level.run() command found in level/levels.py
            self.screen.blit(time, (700, 25))
            self.screen.blit(score, (700, 50))

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
        if self.keys[pygame.K_c] and settings.death:
            # Reset variables
            settings.score = 0
            self.deathTime = round(self.time / 1000)
            settings.death = False
            self.game = False
            # Run game
            self.level = Level(self.screen)
            SuperJumpWorld().startup(self.keys)

    def onFinish(self):
        """
        When the player has reached the end of the level
        This function handles what happens after
        """
        # Images
        endScreen = visualizationService.get_endScreen()
        # Drawing
        self.screen.blit(endScreen, endScreen.get_rect())
        # Restart game
        print(f"Score: {settings.score}\nTime: {self.time / 1000 - self.deathTime}")
        if self.keys[pygame.K_c] and settings.finish:
            soundService.get_applause()
            # Reset variables
            settings.score = 0
            settings.finish = False
            self.deathTime = round(self.time / 1000)
            self.game = False
            # Run game
            self.level = Level(self.screen)
            SuperJumpWorld().startup(self.keys)


if __name__ == "__main__":
    SuperJumpWorld().initialize()
