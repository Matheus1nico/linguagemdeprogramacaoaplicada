from code.enemy import Enemy
from code.entity import Entity

class EntitiesMediator:
    @staticmethod
    def __verify_window_collision(ent: Entity): # '__' = signal for a private method
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0

    @staticmethod
    def collision_verify(entity_list: list[Entity]):
        for i in range(len(entity_list)):
             entity_test = entity_list[i]
             EntitiesMediator.__verify_window_collision(entity_test)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)