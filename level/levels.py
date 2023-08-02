import pygame

from level.settings import tileSize
from level.tile_maker import Tile
from services.player import Player


class Level:
    def __init__(self, levelData, surface):
        # level setup
        self.displaySurface = surface
        self.setupLevel(levelData)
        self.worldShift = 0

    def setupLevel(self, layout):
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

    def run(self):
        # Level tiles
        self.tiles.update(self.worldShift)
        self.tiles.draw(self.displaySurface)
        # Player
        self.player.update()
        self.player.draw(self.displaySurface)
