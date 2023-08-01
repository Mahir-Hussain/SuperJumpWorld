import pygame

from services.level.settings import tile_size
from services.level.tile import Tile


class Level:
    def __init__(self, level_data, surface):
        self.displaySurface = surface
        self.setupLevel(level_data)

    def setupLevel(self, layout):
        self.tiles = pygame.sprite.Group()
        for rowIndex, row in enumerate(layout):
            for colIndex, cell in enumerate(row):
                if cell == "X":
                    x, y = colIndex * tile_size, rowIndex * tile_size
                    tiles = Tile((x, y), tile_size)
                    self.tiles.add(tiles)

    def run(self):
        self.tiles.draw(self.displaySurface)
