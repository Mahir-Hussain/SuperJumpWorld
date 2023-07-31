import pygame
from pygame.image import *
from pygame.locals import *

from sys import exit
import time


class SuperJumpWorld():
    def __init__(self):
        pygame.init()
        self.width = 500
        self.height = 500
        self.name = pygame.display.set_caption("Super Jump World")
        self.icon = pygame.display.set_icon(pygame.image.load('images/icon.png'))
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.keys = pygame.key.get_pressed()
        self.clock = pygame.time.Clock()

    def initialize(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            if self.keys[K_p]:
                

    def updater(self, data):
        self.screen.fill([255,255,255])

        image, rect = data
        self.screen.blit(image, rect)

        pygame.display.update()
        self.clock.tick(60)

    def startup(self):
        menuImg = pygame.image.load("images\start-up.png").convert()
        pygame.transform.scale(menuImg, (self.width, self.height))
        rect = menuImg.get_rect()

        self.updater((menuImg, rect))
        while pygame.key.get_pressed()[pygame.K_p] == 0:
            return
        else:
            self.menu()

    def menu(self):
        menuImg = pygame.image.load("images\menu.png").convert()
        pygame.transform.scale(menuImg, (self.width, self.height))
        rect = menuImg.get_rect()

        self.updater((menuImg, rect))
        while pygame.key.get_pressed()[pygame.K_1] == 0:
            return
        print("done")
        time.sleep(10)
        exit()

SuperJumpWorld().initialize()