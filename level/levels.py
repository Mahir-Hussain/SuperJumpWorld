import pygame
from pytmx.util_pygame import load_pygame

import level.settings as settings
from level.settings import tileSize
from level.tile_maker import Tile
from services.collider import colliderTile
from services.enemy import Enemy
from services.player import Player
from services.sound_service import soundService


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
        # Characters
        self.player = pygame.sprite.GroupSingle()
        self.enemies = pygame.sprite.Group()
        # Level
        self.collision = pygame.sprite.Group()
        self.collectables = pygame.sprite.Group()
        self.end = pygame.sprite.Group()
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
                    self.enemies.add(enemy)
            if layer.name == "blockers":
                for x, y, surf in layer.tiles():
                    colliders = colliderTile((x * tileSize, y * tileSize))
                    self.collision.add(colliders)
            if layer.name == "end-detection":
                for x, y, surf in layer.tiles():
                    end = colliderTile((x * tileSize, y * tileSize))
                    self.end.add(end)
            if layer.name == "collectables":
                for x, y, surf in layer.tiles():
                    collectables = colliderTile((x * tileSize, y * tileSize))
                    self.collectables.add(collectables)

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
            playerX > 380
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
        for enemy in self.enemies.sprites():
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
            for enemy in self.enemies.sprites():
                if enemy.rect.colliderect(blockers.rect):
                    enemy.handlemovement()

        # To check if the player has reached the end of the level
        for sprite in self.end.sprites():
            if sprite.rect.colliderect(player.rect):
                settings.finish = True

    def collisionY(self):
        """
        Handles collisions in the Y direction
        """
        # Player Y
        player = self.player.sprite
        player.rect.y += player.direction.y
        player.gravity()
        # Enemy Y
        for enemy in self.enemies.sprites():
            enemy.rect.y += enemy.direction.y
            enemy.gravity()

        for sprite in self.tiles.sprites():  # Player tile detecion
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.jump = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

        for enemy in self.enemies.sprites():  # Enemy tile detection
            for sprite in self.tiles.sprites():
                if sprite.rect.colliderect(enemy.rect):
                    if enemy.direction.y > 0:
                        enemy.rect.bottom = sprite.rect.top
                        enemy.direction.y = 0
                        enemy.jump = True
                    elif player.direction.y < 0:
                        enemy.rect.top = sprite.rect.bottom
                        enemy.direction.y = 0

    def checkEnemyCollision(self):
        """
        Checks how the player hits the enemy
        If it is from above, kill the enemy
        if from any other direction, kill player.
        """
        enemyCollision = pygame.sprite.spritecollide(
            self.player.sprite, self.enemies.sprites(), False
        )  # Returns a list of when the enemy and the player collide

        if enemyCollision:
            for enemy in enemyCollision:
                enemyCenter = enemy.rect.centery
                enemyTop = enemy.rect.top
                playerBottom = self.player.sprite.rect.bottom
                if (
                    enemyTop < playerBottom < enemyCenter
                    and self.player.sprite.direction.y >= 0
                ):
                    enemy.rect.x += 10000
                    soundService.get_enemyDeath()
                    settings.score += 1

                else:
                    self.player.sprite.rect.y = 1000

    def checkCollectablecollision(self):
        """
        Checks if the player hits a collectable tile
        """
        player = self.player.sprite
        for sprite in self.collectables.sprites():
            if sprite.rect.colliderect(player.rect):
                settings.score += 1
                sprite.rect.x += 100000

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
        self.checkCollectablecollision()
        # Enemy
        self.enemies.update(self.worldShift)
        self.enemies.draw(self.displaySurface)
        # Hitbox
        self.checkEnemyCollision()
        # Collisions
        self.collisionX()
        self.collisionY()
        self.collision.update(self.worldShift)
        self.collectables.update(self.worldShift)
        self.end.update(self.worldShift)
