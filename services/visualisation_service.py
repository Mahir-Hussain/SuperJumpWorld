import os

import pygame


class visualizationService:
    @staticmethod
    def get_icon():
        return pygame.image.load(os.path.join("images", "icon.png")).convert()

    @staticmethod
    def get_startup():
        return pygame.image.load(os.path.join("images", "start-up.png")).convert()

    @staticmethod
    def get_menu():
        return pygame.image.load(os.path.join("images", "menu.png")).convert()

    @staticmethod
    def get_lemon_character():
        return pygame.image.load(os.path.join("images", "lemon-egg.png"))

    @staticmethod
    def get_world1(needs=False):
        ground = pygame.image.load(os.path.join("images\world-1", "ground.png"))
        sky = pygame.image.load(os.path.join("images\world-1", "sky.png"))
        pyramids = pygame.image.load(os.path.join("images\world-1", "pyramids.png"))
        if needs == "all":
            return ground, pyramids, sky
        if needs == "sky":
            return sky
        if needs == "ground":
            return ground
        if needs == "pyramids":
            return pyramids
