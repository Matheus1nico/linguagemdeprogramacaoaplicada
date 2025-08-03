import pygame

#COLORS
ORANGE_COLOR = (255, 128, 0)
WHITE_COLOR = (255, 255, 255)
YELLOW_COLOR = (255,255,0)

#M
MENU_OPTIONS = ('UM JOGADOR', 'DOIS JOGADORES - COOPERATIVO', 'DOIS JOGADORES - COMPETITIVO', 'PONTUAÇÕES', 'SAIR')

#entities speeds
ENTITY_SPEED = {'Level1Bg0': 0,'Level1Bg1': 1,'Level1Bg2': 1,'Level1Bg3': 3,'Level1Bg4': 4,'Level1Bg5': 5,'Level1Bg6': 6, 'Enemy1': 1, 'Enemy2': 2}
PLAYER_SPEED = 3
#Enemy Spawn Event
ENEMY_EVENT = pygame.USEREVENT + 1
ENEMY_SPAWN_TIME = 4000

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
             'Player2': pygame.K_SPACE}

#WINDOW SIZES
WIN_WIDTH = 576
WIN_HEIGHT = 324
