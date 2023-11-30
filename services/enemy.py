from random import choice, randint

import pygame

from services.visualisation_service import visualizationService


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        # Image
        self.enemy = randint(1, 3)
        self.image = self.randomEnemy()
        self.rect = self.image.get_rect(topleft=pos)
        # self.rect = pygame.rect.Rect(pos, (100, 32))
        # Player movement
        self.movement = choice(["right", "left"])
        self.direction = pygame.math.Vector2(0, 0)
        self.jump = True
        self.jumpCount = 0
        self.jumpMax = 25
        # Velocities
        self.velocity = 5
        self.gravityVel = 4
        print(self.rect)

    def randomEnemy(self):
        return visualizationService.get_enemy(img=self.enemy, orientation="right")

    def orientation(self, orientation):
        """
        This function change the enemy
        image when they move left/right
        """
        self.image = visualizationService.get_enemy(self.enemy, orientation)

    def enemyMovement(self):
        """
        Change the enemy movement
        based on a variable changed
        during a block collision
        """
        if self.movement == "right":
            self.direction.x = 1
            self.orientation("right")
        elif self.movement == "left":
            self.direction.x = -1
            self.orientation("left")

    def handlemovement(self):
        if self.movement == "right":
            self.movement = "left"
        elif self.movement == "left":
            self.movement = "right"

    def jumpMechanic(self):
        """
        Allows the enemy to jump.
        This functionality is not added
        at the minute
        """
        self.jumpCount = self.jumpMax
        if self.jump:
            self.direction.y -= self.jumpCount
            if self.jumpCount > -self.jumpMax:
                self.jumpCount -= 1
        self.jump = False

    def gravity(self):
        self.direction.y -= -self.gravityVel
        self.rect.y += self.direction.y

    def kill(self):
        self.rect.y = 1000

    def update(self, xShift):
        """
        Handles how the enemy moves in regard to left
        and right and how the level moves
        """
        self.rect.x += xShift
        self.enemyMovement()
