import pygame

from level.settings import screenWidth, tileSize
from level.tile_maker import Tile
from services.enemy import Enemy
from services.player import Player


class Level:  # Creates the level using settings.py
    def __init__(self, levelData, surface):
        # level setup
        self.displaySurface = surface
        self.setupLevel(levelData)
        self.worldShift = 0  # Moves depending on player

    def setupLevel(self, layout):  # Loops over levelMap to add tiles
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.enemy = pygame.sprite.Group()
        for rowIndex, row in enumerate(layout):
            for colIndex, col in enumerate(row):
                x = colIndex * tileSize
                y = rowIndex * tileSize
                if col == "G":  # Adds grass
                    tile = Tile((x, y), col)
                    self.tiles.add(tile)
                if col == "S":  # Adds stone
                    tile = Tile((x, y), col)
                    self.tiles.add(tile)
                if col == "U":  # Adds "under-grass"
                    tile = Tile((x, y), col)
                    self.tiles.add(tile)
                if col == "M":  # Adds mysterybox
                    tile = Tile((x, y), col)
                    self.tiles.add(tile)
                if col == "P":  # "Adds the player
                    playerSprite = Player((x, y))
                    self.player.add(playerSprite)
                if col == "E":
                    enemySprite = Enemy((x, y))
                    self.enemy.add(enemySprite)

    def levelMovement(self):  # Moves the level around the player
        player = self.player.sprite
        playerX = player.rect.centerx
        direction = player.rect.x

        if playerX < 175 and direction < 0 and player.movement == True:
            self.worldShift = 7
            player.velocity = 0
        elif (
            playerX > 350
            and direction > 0
            and player.movement == True
            and player.left == False
        ):
            self.worldShift = -7
            player.velocity = 0
        else:
            self.worldShift = 0
            player.velocity = 7

    def collisionX(self):  # Collisions in X direction
        player = self.player.sprite
        player.rect.x += player.direction.x * player.velocity

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def collisionY(self):  # Collision in Y direction
        # Player Y
        player = self.player.sprite
        player.rect.y += player.direction.y
        player.gravity()
        # Enemy Y
        enemy = self.enemy_sprites
        enemy.rect.y += enemy.direction.y
        enemy.gravity()

        for sprite in self.tiles.sprites():  # Player
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.jump = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

        for sprite in self.tiles.sprites():  # Enemy
            if sprite.rect.colliderect(enemy.rect):
                if enemy.direction.y > 0:
                    enemy.rect.bottom = sprite.rect.top
                    enemy.direction.y = 0
                    enemy.jump = True
                elif player.direction.y < 0:
                    enemy.rect.top = sprite.rect.bottom
                    enemy.direction.y = 0
            #
            a = pygame.sprite.spritecollide(self.player.sprite, self.enemy_sprites, True)
            print(a)
            # hit = pygame.sprite.spritecollide(self.enemy, self.player, True)  #
            # print(hit)

    def run(self):  # Where all the drawing comes together
        # Level tiles
        self.tiles.update(self.worldShift)
        self.tiles.draw(self.displaySurface)
        self.levelMovement()
        # Player
        self.player.update()
        self.player.draw(self.displaySurface)
        # Enemy
        self.enemy.draw(self.displaySurface)
        self.enemy.update()
        # Collisions
        self.collisionX()
        self.collisionY()
