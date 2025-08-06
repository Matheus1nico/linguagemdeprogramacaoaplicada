from abc import ABC, abstractmethod
import pygame.image

from code.const import ENTITIES_HEALTH


class Entity(ABC):

    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./assets/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left = position[0], top = position[1])
        self.speed = 0
        self.health = ENTITIES_HEALTH[self.name]
        self.entityShoot = pygame.image.load('./assets/' + name + '.png').convert_alpha()

    @abstractmethod
    def move(self):
        pass