import pygame.key
from code.const import WIN_HEIGHT, PLAYER_SPEED, WIN_WIDTH, PLAYER_UP, PLAYER_DOWN, PLAYER_LEFT, PLAYER_RIGHT, PLAYER_SHOOT
from code.entity import Entity

class Player(Entity):
    def __init__(self, name: str, position: tuple, ):
        super().__init__(name, position)

    def move(self,):
        #WASD player movement
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= PLAYER_SPEED
        if pressed_key[PLAYER_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += PLAYER_SPEED
        if pressed_key[PLAYER_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= PLAYER_SPEED
        if pressed_key[PLAYER_RIGHT[self.name] ] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += PLAYER_SPEED
        pass