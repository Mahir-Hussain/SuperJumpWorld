import pygame
from pytmx.util_pygame import load_pygame

from level.settings import tileSize
from level.tile_maker import Tile
from services.enemy import Enemy
from services.player import Player


class Level:  # Creates the level using settings.py
    def __init__(self, surface):
        # level setup
        self.displaySurface = surface
        self.setupLevel()
        self.worldShift = 0  # Moves depending on player

    def setupLevel(self):
        """
        Adds player and enemy to the level
        This gets the level data from the tmx file
        and adds the tiles to the screen
        """
        # Tile groups
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        # TMX info
        self.tmx_data = load_pygame("level\levelMap\level1.tmx")
        # Adding tiles to screen
        for layer in self.tmx_data.layers:
            if layer.name == "terrain":
                for x, y, surf in layer.tiles():
                    tile = Tile((x * tileSize, y * tileSize), surf)
                    self.tiles.add(tile)
        playerSprite = Player((0, 0))
        self.player.add(playerSprite)

    def levelMovement(self):
        """
        This moves the level around the player
        """
        player = self.player.sprite
        playerX = player.rect.centerx
        direction = player.rect.x

        if playerX < 175 and direction < 0 and player.movement == True:
            self.worldShift = 7
            player.velocity = 0
        elif (
            playerX > 350
            and direction > 0
            and player.movement == True
            and player.left == False
        ):
            self.worldShift = -7
            player.velocity = 0
        else:
            self.worldShift = 0
            player.velocity = 7

    def collisionX(self):
        """
        Handles collisions in the X direction
        """
        # Player X
        player = self.player.sprite
        player.rect.x += player.direction.x * player.velocity
        # Player Y
        # enemy = self.enemy.sprite
        # enemy.rect.x += enemy.direction.x * enemy.velocity

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def collisionY(self):
        """
        Handles collisions in the Y direction
        """
        # Player Y
        player = self.player.sprite
        player.rect.y += player.direction.y
        player.gravity()
        # Enemy Y
        # enemy = self.enemy.sprite
        # enemy.rect.y += enemy.direction.y
        # enemy.gravity()

        for sprite in self.tiles.sprites():  # Player
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.jump = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

        # for sprite in self.tiles.sprites():  # Enemy
        #     if sprite.rect.colliderect(enemy.rect):
        #         if enemy.direction.y > 0:
        #             enemy.rect.bottom = sprite.rect.top
        #             enemy.direction.y = 0
        #             enemy.jump = True
        #         elif player.direction.y < 0:
        #             enemy.rect.top = sprite.rect.bottom
        #             enemy.direction.y = 0

        #     if enemy.rect.colliderect(player):
        #         enemy.yeet()

    def run(self):
        """
        Where all the drawing comes together.
        All functions found in this class is called here.
        The run function is called in main.py
        """
        # Level tiles
        self.tiles.update(self.worldShift)
        self.tiles.draw(self.displaySurface)
        self.levelMovement()
        # Player
        self.player.update()
        self.player.draw(self.displaySurface)
        # Enemy
        # self.enemy.update()
        # self.enemy.draw(self.displaySurface)
        # Collisions
        self.collisionX()
        self.collisionY()
