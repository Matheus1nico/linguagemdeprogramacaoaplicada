import pygame

#COLORS
ORANGE_COLOR = (255, 128, 0)
WHITE_COLOR = (255, 255, 255)
YELLOW_COLOR = (255,255,0)

#M
MENU_OPTIONS = ('UM JOGADOR', 'DOIS JOGADORES - COOPERATIVO', 'DOIS JOGADORES - COMPETITIVO', 'PONTUAÇÕES', 'SAIR')

#entities speeds
ENTITY_SPEED = {'Level1Bg0': 0,'Level1Bg1': 1,'Level1Bg2': 1,'Level1Bg3': 3,'Level1Bg4': 4,'Level1Bg5': 5,'Level1Bg6': 6, 'Enemy1': 1, 'Enemy2': 2, 'Player1Shot': 4, 'Player2Shot': 4, 'Enemy1Shot': 6, 'Enemy2Shot': 6,}

PLAYER_SPEED = 3
#Enemy Spawn Event
ENEMY_EVENT = pygame.USEREVENT + 1
ENEMY_SPAWN_TIME = 4000

#Entities Health
ENTITIES_HEALTH = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Player1': 100,
    'Player2': 100,
    'Enemy1': 50,
    'Enemy2': 60,
    'Player1Shot': 1,
    'Player2Shot': 1,
    'Enemy1Shot': 1,
    'Enemy2Shot': 1
}
#Shooting delay for entities
ENTITIES_SHOOT_DELAY = {
    'Player1': 15,
    'Player2': 15,
    'Enemy1': 80,
    'Enemy2': 80,
}

ENTITIES_DAMAGES = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Player1': 10,
    'Player2': 10,
    'Enemy1': 10,
    'Enemy2': 10,
    'Player1Shot': 30,
    'Player2Shot': 25,
    'Enemy1Shot': 15,
    'Enemy2Shot': 15
}

#Gameplay keys
PLAYER_UP = {'Player1': pygame.K_w,
             'Player2': pygame.K_UP}
PLAYER_DOWN = {'Player1': pygame.K_s,
             'Player2': pygame.K_DOWN}
PLAYER_LEFT = {'Player1': pygame.K_a,
             'Player2': pygame.K_LEFT}
PLAYER_RIGHT = {'Player1': pygame.K_d,
             'Player2': pygame.K_RIGHT}
PLAYER_SHOOT = {'Player1': pygame.K_SPACE,
             'Player2': pygame.K_RCTRL}

#WINDOW SIZES
WIN_WIDTH = 576
WIN_HEIGHT = 324
