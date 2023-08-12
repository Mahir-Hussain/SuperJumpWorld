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
        self.jumpVel = 100
        self.gravityVel = 4
        self.direction = pygame.math.Vector2(0, 0)
        self.movement = False
        self.jump = True

    def orientation(self, orientation):  # Changes the player image when pressing A,D
        self.image = visualizationService.get_lemon_character(orientation)

    def playerMovement(self):
        keyPressed = pygame.key.get_pressed()
        self.movement = False

        if keyPressed[pygame.K_a] and self.rect.x - self.velocity > 0:
            self.orientation("left")
            self.movement = True
            self.direction.x = -1
            self.left = True
        elif keyPressed[pygame.K_d]:
            self.orientation("right")
            self.movement = True
            self.direction.x = 1
            self.left = False
        else:
            self.direction.x = 0

        if keyPressed[pygame.K_w] and self.jump:
            # if self.direction.y == 0:
            # self.direction.y = -self.jumpVel
            # self.jump = False
            self.jumpMechanic()
        elif keyPressed[pygame.K_s]:
            self.direction.y = self.jumpVel
        else:
            self.direction.y = 0

    def jumpMechanic(self):  # Player jumping
        self.direction.y = -self.jumpVel
        self.jump = False

    def gravity(self):  # Applies gravity to the player
        self.direction.y -= -self.gravityVel
        self.rect.y += self.direction.y

    def update(self):
        self.playerMovement()
        # self.rect.x += self.direction.x * self.velocity
        # self.rect.y += self.direction.y
        # self.gravity()
