import pygame


class colliderTile(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((37, 37))
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, xShift):
        """
        Handles how the enemy moves in regard to left
        and right and how the level moves
        """
        self.rect.x += xShift
