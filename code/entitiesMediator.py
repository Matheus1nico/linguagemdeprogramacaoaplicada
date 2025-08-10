from code.const import WIN_WIDTH
from code.enemy import Enemy
from code.entity import Entity
from code.player import Player
from enemyshot import EnemyShot
from playershot import PlayerShot


class EntitiesMediator:
    @staticmethod
    def __verify_window_collision(ent: Entity): # '__' = signal for private method
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0
        if isinstance(ent, PlayerShot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0
        if isinstance(ent, EnemyShot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0

    @staticmethod
    def __verify_entity_collision(ent1, ent2):
        collided = False
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot):
            collided = True
        elif isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):
            collided = True
        elif isinstance(ent1, Player) and isinstance(ent2, EnemyShot):
            collided = True
        elif isinstance(ent1, EnemyShot) and isinstance(ent2, Player):
            collided = True

        if collided: # used as if collided == True
            if ent1.rect.right >= ent2.rect.left and ent1.rect.left <= ent2.rect.right and ent1.rect.bottom >= ent2.rect.top and ent1.rect.top <= ent2.rect.bottom:
                ent1.health -= ent2.damage
                ent2.health -= ent1.damage
                ent1.last_damage = ent2.name
                ent2.last_damage = ent1.name

    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        pass

    @staticmethod
    def collision_verify(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntitiesMediator.__verify_window_collision(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntitiesMediator.__verify_entity_collision(entity1, entity2)

    @staticmethod
    def health_verify(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    EntitiesMediator.__give_score(ent, entity_list)
                entity_list.remove(ent)