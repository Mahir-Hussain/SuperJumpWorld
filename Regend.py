import pygame
from pygame.locals import *

import os
from sys import exit

def character():
    lemon = pygame.image.load(
        os.path.join("images", "lemon-egg.png")
    )

    character = pygame.transform.scale(lemon, (80, 80))
    rect = pygame.Rect(100, 300, 500, 500)

    return character, rect

class SuperJumpWorld():
    def __init__(self):
        self.width = 500
        self.height = 500
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.name = pygame.display.set_caption("Super Jump World")
        self.icon = pygame.display.set_icon(pygame.image.load('images/icon.png'))

    def initialize(self):

        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   exit()


            self.screenUpdater(character, rect)

    def screenUpdater(self, character, rect):

        self.screen.fill((255, 255, 255))
        self.screen.blit(character, (rect.x, rect.y))

        pygame.display.update()

    def playerMovement(self, keyPressed):
        print("1")


if __name__ == "__main__":
    SuperJumpWorld().initialize()