import pygame

from services.visualisation_service import visualizationService


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        # Player image
        self.image = visualizationService.get_lemon_character("right")
        self.rect = self.image.get_rect(topleft=pos)
        # Player movement
        self.velocity = 2
        self.jumpVel = 6
        self.gravityVel = 4
        self.direction = pygame.math.Vector2(0, 0)
        self.movement = False

    def playerMovement(self):
        keyPressed = pygame.key.get_pressed()
        # print(self.movement)
        self.movement = False

        if keyPressed[pygame.K_a] and self.rect.x - self.velocity > 0:
            self.orientation = visualizationService.get_lemon_character("left")
            self.movement = True
            self.direction.x = -1
        elif keyPressed[pygame.K_d]:
            self.orientation = visualizationService.get_lemon_character("right")
            self.movement = True
            self.direction.x = 1
        else:
            self.direction.x = 0

        if keyPressed[pygame.K_w]:
            # if self.direction.y == 0:
            self.direction.y = -self.jumpVel
            self.movement = True
        elif keyPressed[pygame.K_s]:
            self.direction.y = self.jumpVel
            self.movement = True
        else:
            self.direction.y = 0

    def gravity(self):  # Applies gravity to the player
        self.direction.y -= -self.gravityVel
        self.rect.y += self.direction.y

    def update(self):
        self.playerMovement()
        # self.rect.x += self.direction.x * self.velocity
        # self.rect.y += self.direction.y
        # self.gravity()
