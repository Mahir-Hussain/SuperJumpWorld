import pygame

from services.visualisation_service import visualizationService


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        # Player image
        self.image = visualizationService.get_lemon_character("right")
        self.rect = self.image.get_rect(topleft=pos)
        # Player movement
        self.velocity = 5
        self.jumpVel = 6
        self.gravityVel = 3
        self.direction = pygame.math.Vector2(0, 0)

    def playerMovement(self):
        keyPressed = pygame.key.get_pressed()
        if keyPressed[pygame.K_a] and self.rect.x - self.velocity > 0:
            self.direction.x = -1
            self.orientation = visualizationService.get_lemon_character("left")
        elif keyPressed[pygame.K_d]:
            self.direction.x = 1
            self.orientation = visualizationService.get_lemon_character("right")
        else:
            self.direction.x = 0
        if keyPressed[pygame.K_w]:
            # if self.direction.y == 0:
            self.direction.y = -self.jumpVel
        elif keyPressed[pygame.K_s]:
            self.direction.y = self.jumpVel
        else:
            self.direction.y = 0

    def gravity(self):
        self.direction.y -= -self.gravityVel
        self.rect.y += self.direction.y

    def update(self):
        self.playerMovement()
        self.rect.x += self.direction.x * self.velocity
        # self.rect.y += self.direction.y
        # self.gravity()
