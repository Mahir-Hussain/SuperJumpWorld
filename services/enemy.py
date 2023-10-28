import pygame

from services.visualisation_service import visualizationService


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        # Image
        self.image = visualizationService.get_enemy()
        self.rect = self.image.get_rect(topleft=pos)
        # Player movement
        self.direction = pygame.math.Vector2(0, 0)
        self.jump = True
        self.jumpCount = 0
        self.jumpMax = 25
        # Velocities
        self.velocity = 7
        self.gravityVel = 4

    def enemyMovement(self):
        keyPressed = pygame.key.get_pressed()
        self.movement = False

        if keyPressed[pygame.K_l]:  # and self.rect.x - self.velocity > 0:
            self.movement = True
            self.direction.x = -1
            self.left = True
        elif keyPressed[pygame.K_k]:
            self.movement = True
            self.direction.x = 1
            self.left = False
        else:
            self.direction.x = 0

        if keyPressed[pygame.K_UP] and self.jump and self.rect.y - self.jumpMax > 0:  #
            self.jumpMechanic()

    def jumpMechanic(self):  # Enemy jumping
        self.jumpCount = self.jumpMax
        if self.jump:
            self.direction.y -= self.jumpCount
            if self.jumpCount > -self.jumpMax:
                self.jumpCount -= 1
        self.jump = False

    def gravity(self):
        self.direction.y -= -self.gravityVel
        self.rect.y += self.direction.y

    def yeet(self):
        self.rect.y = 1000

    def update(self):
        self.enemyMovement()
