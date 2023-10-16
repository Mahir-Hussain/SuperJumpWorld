import os

import pygame


class soundService:
    @staticmethod
    def get_jump():
        jump = pygame.mixer.Sound(os.path.join("sound", "jump.mp3"))
        pygame.mixer.Sound.play(jump)

    @staticmethod
    def get_death():
        death = pygame.mixer.Sound(os.path.join("sound", "death.mp3"))
        pygame.mixer.Sound.play(death)

    @staticmethod
    def get_background():
        pygame.mixer.music.load(os.path.join("sound", "background.mp3"))
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.1)
