from code.menu import Menu

import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(800, 600))

    def run(self):
         while True:
            menu = Menu(self.window)
            menu.run()
            print('Start Setup')
            print('Ending Setup')

            print('Starting Loop')
            while True:
                # check for all events
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        print('Closing Window')
                        pygame.quit()  # close window
                        quit()  # end pygame