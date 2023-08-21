import pygame

from services.visualisation_service import visualizationService


class Tile(pygame.sprite.Sprite):  # Places tiles in the window
    def __init__(self, pos, tileType):
        super().__init__()
        self.image = self.tiler(
            tileType
        )  # Changes image depending on letter given from level.setupLevel()
        self.rect = self.image.get_rect(topleft=pos)  # Gets a rect value

    def update(self, xShift):  # Moves the world based on player movement
        self.rect.x += xShift

    def tiler(self, tileType):  # Returns a different tile depending on input
        if tileType == "G":
            return visualizationService.get_grass()
        elif tileType == "U":
            return visualizationService.get_underGrass()
        elif tileType == "S":
            return visualizationService.get_stone()
        elif tileType == "M":
            return visualizationService.get_mbox()
