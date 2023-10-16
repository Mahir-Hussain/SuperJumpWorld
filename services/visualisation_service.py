import os

import pygame


class visualizationService:  # Loads images to other files. Can be used to get_rect as well
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
    def get_lemon_character(orientation="right"):
        lemon = pygame.image.load(os.path.join("images/characters", "lemon-egg.png"))
        lemon = pygame.transform.scale(lemon, (60, 50))
        if orientation == "right":
            return lemon
        elif orientation == "left":
            return pygame.transform.flip(lemon, True, False)

    @staticmethod
    def get_mbox():
        return pygame.image.load(os.path.join("images/tiles", "mbox.png"))

    @staticmethod
    def get_grass():
        return pygame.image.load(os.path.join("images/tiles", "grass.png"))

    @staticmethod
    def get_underGrass():
        return pygame.image.load(os.path.join("images/tiles", "under-grass.png"))

    @staticmethod
    def get_stone():
        return pygame.image.load(os.path.join("images/tiles", "stone.png"))

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

    @staticmethod
    def get_enemy():
        enemy = pygame.image.load(os.path.join("images\characters", "enemy-sword.png"))
        enemy = pygame.transform.scale(enemy, (60, 50))
        return enemy

    @staticmethod
    def get_gameOver():
        return pygame.image.load(os.path.join("images\extras"), "game-over.png")
