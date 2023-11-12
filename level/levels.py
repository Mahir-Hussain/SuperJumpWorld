import pygame
from pytmx.util_pygame import load_pygame

import level.settings as settings
from level.settings import tileSize
from level.tile_maker import Tile
from services.collider import colliderTile
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
        self.enemy = pygame.sprite.Group()
        self.collision = pygame.sprite.Group()
        self.deathtiles = pygame.sprite.Group()
        # TMX info
        self.tmx_data = load_pygame("level\levelMap\level1.tmx")
        # Adding tiles to screen
        for layer in self.tmx_data.layers:
            if layer.name == "terrain":
                for x, y, surf in layer.tiles():
                    tile = Tile((x * tileSize, y * tileSize), surf)
                    self.tiles.add(tile)
            if layer.name == "player":
                for x, y, surf in layer.tiles():
                    playerSprite = Player((x * tileSize, y * tileSize))
                    self.player.add(playerSprite)
            if layer.name == "enemies":
                for x, y, surf in layer.tiles():
                    enemy = Enemy((x * tileSize, y * tileSize))
                    self.enemy.add(enemy)
            if layer.name == "blockers":
                for x, y, surf in layer.tiles():
                    colliders = colliderTile((x * tileSize, y * tileSize))
                    self.collision.add(colliders)

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
        # Player X movement
        player = self.player.sprite
        player.rect.x += player.direction.x * player.velocity
        # Enemy X movement
        for enemy in self.enemy.sprites():
            enemy.rect.x += enemy.direction.x * enemy.velocity

        # Player collision
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

        # Enemy collision (used to change direction)
        for blockers in self.collision.sprites():
            for enemy in self.enemy.sprites():
                if enemy.rect.colliderect(blockers.rect):
                    enemy.handlemovement()

    def collisionY(self):
        """
        Handles collisions in the Y direction
        """
        # Player Y
        player = self.player.sprite
        player.rect.y += player.direction.y
        player.gravity()
        # Enemy Y
        for x in self.enemy.sprites():
            # enemy = self.enemy.sprites
            x.rect.y += x.direction.y
            x.gravity()

        for sprite in self.tiles.sprites():  # Player
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.jump = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

        for enemy in self.enemy.sprites():
            for sprite in self.tiles.sprites():  # Enemy
                if sprite.rect.colliderect(enemy.rect):
                    if enemy.direction.y > 0:
                        enemy.rect.bottom = sprite.rect.top
                        enemy.direction.y = 0
                        enemy.jump = True
                    elif player.direction.y < 0:
                        enemy.rect.top = sprite.rect.bottom
                        enemy.direction.y = 0

                if enemy.rect.colliderect(player):
                    enemy.yeet()

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
        self.enemy.update(self.worldShift)
        self.enemy.draw(self.displaySurface)
        # Collisions
        self.collisionX()
        self.collisionY()
        self.collision.update(self.worldShift)
