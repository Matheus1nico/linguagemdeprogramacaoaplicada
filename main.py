import pygame

print('Start Setup')
pygame.init()
janela = pygame.display.set_mode(size=(800,600))
print('Ending Setup')

print('Starting Loop')
while True:
    #check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #close window
            quit() #end pygame