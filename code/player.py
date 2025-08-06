import pygame.key
from code.const import WIN_HEIGHT, PLAYER_SPEED, WIN_WIDTH, PLAYER_UP, PLAYER_DOWN, PLAYER_LEFT, PLAYER_RIGHT, \
    PLAYER_SHOOT, ENTITIES_SHOOT_DELAY
from code.entity import Entity
from playershot import PlayerShot


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shootDelay = ENTITIES_SHOOT_DELAY[self.name]

    def move(self,):
        #WASD player movement
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= PLAYER_SPEED
        if pressed_key[PLAYER_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += PLAYER_SPEED
        if pressed_key[PLAYER_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= PLAYER_SPEED
        if pressed_key[PLAYER_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += PLAYER_SPEED
        pass

    def shoot(self):
        self.shootDelay -= 1
        if self.shootDelay == 0:
            self.shootDelay = ENTITIES_SHOOT_DELAY[self.name]
            pressed_key = pygame.key.get_pressed()
            if pressed_key[PLAYER_SHOOT[self.name]]:
                return PlayerShot(name = f'{self.name}Shot', position = (self.rect.centerx, self.rect.centery))