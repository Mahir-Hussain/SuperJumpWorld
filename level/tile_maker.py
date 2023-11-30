import pygame

from services.visualisation_service import visualizationService


class Tile(pygame.sprite.Sprite):  # Places tiles in the window
    def __init__(self, pos, tileType):
        super().__init__()
        self.image = tileType  # self.tiler(
        #  tileType
        # )  # Changes image depending on letter given from level.setupLevel()
        self.rect = pygame.rect.Rect(pos, (12, 20))

    def update(self, xShift):
        """
        Moves the world based on player movement
        """
        self.rect.x += xShift
