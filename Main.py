import pygame
from pygame.locals import *

import os
from sys import exit

lemon = pygame.image.load(
    os.path.join("images", "lemon-egg.png")
)
character = pygame.transform.scale(lemon, (80, 80))
rect = pygame.Rect(100, 300, 500, 500)

# def character(dataNeeded=None):
#     lemon = pygame.image.load(
#         os.path.join("images", "lemon-egg.png")
#     )

#     character = pygame.transform.scale(lemon, (80, 80))
#     rect = pygame.Rect(100, 300, 500, 500)

#     if dataNeeded == "rect":
#         return rect
#     elif dataNeeded == "character":
#         return character
#     return character, rect

class SuperJumpWorld():
    def __init__(self):
        self.width = 700
        self.height = 400
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.name = pygame.display.set_caption("Super Jump World")
        self.icon = pygame.display.set_icon(pygame.image.load('images/icon.png'))
        self.velocity = 3
        self.game = False
        self.start = False

    def initialize(self):

        clock = pygame.time.Clock()
        while True:
            keys = pygame.key.get_pressed()
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   exit()

            self.startup(keys)
            if self.game == True:
                self.playerMovement(keys, rect)

                self.screenUpdater(character, rect)

    def startup(self, keyPressed):
        if self.start == False:
            startImg = pygame.image.load("images\start-up.png").convert()
            pygame.transform.scale(startImg, (self.width, self.height))
            rect = startImg.get_rect()

            self.screen.blit(startImg, rect)
            pygame.display.update()

        if keyPressed[pygame.K_p]:
            menuImg = pygame.image.load("images\menu.png").convert()
            pygame.transform.scale(menuImg, (self.width, self.height))
            rect = menuImg.get_rect()

            self.screen.fill((0,0,0))
            self.screen.blit(menuImg, rect)
            pygame.display.update()
            self.start = True
  
        if self.start and keyPressed[pygame.K_1]:
            self.game = True


    def screenUpdater(self, character, rect):

        #character, rect = data

        self.screen.fill((200, 255, 255))
        self.screen.blit(character, (rect.x, rect.y))

        pygame.display.update()

    def playerMovement(self, keyPressed, rect):
        if keyPressed[pygame.K_a]:
            rect.x -= self.velocity
        elif keyPressed[pygame.K_d]:
            rect.x += self.velocity
        if keyPressed[pygame.K_w]:
            rect.y -= self.velocity
        elif keyPressed[pygame.K_s]:
            rect.y += self.velocity
        
        


if __name__ == "__main__":
    SuperJumpWorld().initialize()