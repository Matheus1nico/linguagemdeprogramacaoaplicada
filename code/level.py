import random
import pygame
from pygame import Surface, Rect
from pygame.font import Font
from code.const import WIN_HEIGHT, WHITE_C, MENU_OPTIONS, ENEMY_EVENT, ENEMY_SPAWN_TIME, GREEN_C, CYAN_C, WIN_WIDTH
from code.enemy import Enemy
from code.entitiesMediator import EntitiesMediator
from code.entity import Entity
from code.entityfactory import EntityFactory
from code.player import Player


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        self.timeout = 20000
        if game_mode in [MENU_OPTIONS[1], MENU_OPTIONS[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))
        pygame.time.set_timer(ENEMY_EVENT, ENEMY_SPAWN_TIME)

    def run(self):
        pygame.mixer_music.load(f'./assets/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source = ent.surf, dest = ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)

                #Printed Level Gameplay HUD
                if ent.name == 'Player1':
                    self.level_text(15, f'JOGADOR 1 - Vida: {ent.health} | Pontuação: {ent.score}', GREEN_C, (10, 5))
                if ent.name == 'Player2':
                    self.level_text(15, f'JOGADOR 2 - Vida: {ent.health:} | Pontuação: {ent.score}', CYAN_C, (10, 20))

                #Mostrar FPS no HUD
                #self.level_text(15, f'FPS: {clock.get_fps() :.0f}', WHITE_C, (WIN_WIDTH - 50, 5))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('Closing Window')
                    pygame.quit()  # close window
                    quit()  # end pygame
                    sys.exit()
                if event.type == ENEMY_EVENT:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

            pygame.display.flip()
            #Enemies collisions
            EntitiesMediator.collision_verify(entity_list = self.entity_list)
            EntitiesMediator.health_verify(entity_list = self.entity_list)
            pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_position: tuple):
        text_font: Font = pygame.font.SysFont(name = "Lucida Sans Typewriter", size = text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left = text_position[0], top = text_position[1])
        self.window.blit(source = text_surf, dest = text_rect)
