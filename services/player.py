import pygame

from services.visualisation_service import visualizationService


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.orientation = "right"
        self.image = visualizationService.get_lemon_character(self.orientation)
        self.rect = self.image.get_rect(topleft=pos)
        self.velocity = 5

    def playerMovement(self):
        keyPressed = pygame.key.get_pressed()
        if keyPressed[pygame.K_a] and self.rect.x - self.velocity > 0:
            self.rect.x -= self.velocity
            self.orientation = "right"
        elif keyPressed[pygame.K_d]:
            self.rect.x += self.velocity
            self.orientation = "left"
        if keyPressed[pygame.K_w]:
            self.rect.y -= self.velocity
        elif keyPressed[pygame.K_s]:
            self.rect.y -= -self.velocity

    def update(self):
        self.playerMovement()
