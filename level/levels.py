import pygame

from level.settings import screenWidth, tileSize
from level.tile_maker import Tile
from services.player import Player


class Level:  # Creates the level using settings.py
    def __init__(self, levelData, surface):
        # level setup
        self.displaySurface = surface
        self.setupLevel(levelData)
        self.worldShift = 0  # Moves depending on player

    def setupLevel(self, layout):  # Loops over levelMap to add tiles
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for rowIndex, row in enumerate(layout):
            for colIndex, col in enumerate(row):
                x = colIndex * tileSize
                y = rowIndex * tileSize
                if col == "X":
                    tile = Tile((x, y), tileSize)
                    self.tiles.add(tile)
                if col == "P":
                    playerSprite = Player((x, y))
                    self.player.add(playerSprite)

    def levelMovement(self):
        player = self.player.sprite
        playerX = player.rect.centerx
        direction = player.rect.x
        if playerX < screenWidth / 4 and direction < 0:
            self.worldShift = 5
            Player.velocity = 0
        elif playerX > screenWidth - screenWidth / 4 and direction > 0:
            self.worldShift = -5
            Player.velocity = 0
        else:
            self.worldShift = 0
            Player.velocity = 5

    def collisionX(self):  # Collisions in X direction
        player = self.player.sprite
        player.rect.x += player.direction.x * player.velocity

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def collisionY(self):  # Collision in Y direction
        player = self.player.sprite
        player.rect.y += player.direction.y
        player.gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

    def run(self):  # Where all the drawing comes together
        # Level tiles
        self.tiles.update(self.worldShift)
        self.tiles.draw(self.displaySurface)
        self.levelMovement()
        # Player
        self.player.update()
        self.collisionX()
        self.collisionY()
        self.player.draw(self.displaySurface)
