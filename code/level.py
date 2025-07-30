import pygame
from code.entity import Entity
from code.entityfactory import EntityFactory

class Level:

    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))

    def run(self):
        while True:
            for ent in self.entity_list:
                self.window.blit(source = ent.surf, dest = ent.rect)
                ent.move()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        print('Closing Window')
                        pygame.quit()  # close window
                        quit()  # end pygame
            pygame.display.flip()
