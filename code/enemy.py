from code.const import ENTITY_SPEED, WIN_WIDTH, ENTITIES_SHOOT_DELAY
from code.entity import Entity
from enemyshot import EnemyShot


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shootDelay = ENTITIES_SHOOT_DELAY[self.name]

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shootDelay -= 1
        if self.shootDelay == 0:
            self.shootDelay = ENTITIES_SHOOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))