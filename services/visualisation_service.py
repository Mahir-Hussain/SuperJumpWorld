import os

import pygame


class visualizationService:
    """
    Loads images to other files. Can be used to get_rect as well
    """

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
    def get_enemy(img, orientation="right"):
        enemyTypes = {
            1: pygame.image.load(os.path.join("images\characters", "enemy-gun.png")),
            2: pygame.image.load(os.path.join("images\characters", "enemy-sword.png")),
            3: pygame.image.load(os.path.join("images\characters", "enemy-big.png")),
        }
        # Get the correct image and make the enemy larger
        enemy = enemyTypes[img]
        enemy = pygame.transform.scale(enemy, (60, 50))
        # Return correct direction
        if orientation == "left":
            return enemy
        elif orientation == "right":
            return pygame.transform.flip(enemy, True, False)

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
        world = pygame.image.load(os.path.join("images\world-1", "world-1.png"))
        if needs == "all":
            return ground, pyramids, sky
        elif needs == "world":
            return world
        elif needs == "sky":
            return sky
        elif needs == "ground":
            return ground
        elif needs == "pyramids":
            return pyramids

    @staticmethod
    def get_world2(needs=False):
        background = pygame.image.load(os.path.join("images\world-2", "background.png"))
        sky = pygame.image.load(os.path.join("images\world-2", "sky.png"))
        world = pygame.image.load(os.path.join("images\world-2", "world-2.png"))
        if needs == "all":
            return background, sky
        elif needs == "world":
            return world
        elif needs == "background":
            return background
        elif needs == "sky":
            return sky

    @staticmethod
    def get_world3(needs=False):
        background = pygame.image.load(os.path.join("images\world-3", "background.png"))
        sky = pygame.image.load(os.path.join("images\world-3", "sky.png"))
        world = pygame.image.load(os.path.join("images\world-3", "world-3.png"))
        if needs == "all":
            return background, sky
        elif needs == "world":
            return world
        elif needs == "background":
            return background
        elif needs == "sky":
            return sky

    @staticmethod
    def get_gameOver():
        return pygame.image.load(os.path.join("images", "game-over.png"))

    @staticmethod
    def get_endScreen():
        return pygame.image.load(os.path.join("images", "end-screen.png"))
