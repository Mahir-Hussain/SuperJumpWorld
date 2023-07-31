import pygame
from pygame.image import *
from pygame.locals import *
from sys import exit


class SuperJumpWorld():
    def __init__(self):
        self.width = 500
        self.height = 500
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.name = pygame.display.set_caption("Super Jump World")
        self.icon = pygame.display.set_icon(pygame.image.load('images/start-up.png'))
        self.clock = pygame.time.Clock()
        self.counter = 0 # 0 startup, 1 menu

    def data(self):
        data = self.width, self.height, self.screen
        return data

    def initialize(self):
        while True:
            for event in pygame.event.get():
                print(event.type)
                if event.type == 769:
                    self.counter = 1
                    self.game()
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            pygame.display.update()
            self.clock.tick(60)
            self.game()

    def screenChange(self, data):
        self.screen.fill([255,255,255])
        image, rect = data
        self.screen.blit(image, rect)
        pygame.draw.rect(self.screen, "BLACK", rect, 1)
        pygame.display.update()

    def game(self):
        if self.counter == 0:
            self.screenChange(self.startup())
        elif self.counter == 1:
            self.screenChange(menu().menu())

    def startup(self): # Load the start-up image.
        startupImg = pygame.image.load("images\start-up.png").convert() # Optimizes the image for pygame
        pygame.transform.scale(startupImg, (self.width, self.height))
        rect = startupImg.get_rect()

        return startupImg, rect

class menu(SuperJumpWorld):
    def __init__(self):
        self.width, self.height, self.screen = SuperJumpWorld().data()
    
    def menu(self):
        menuImg = pygame.image.load("images\menu.png").convert()
        pygame.transform.scale(menuImg, (self.width, self.height))
        rect = menuImg.get_rect()

        return menuImg, rect

SuperJumpWorld().initialize()