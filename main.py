
'''
Checkers non gui
Edward Abel Guobadia
10-15-2022
'''
from checkers_util import gameboard as gb
import logging
import pygame
import sys


#   main function
def main():
    #   set defualt logging level to DEBUG
    logging.basicConfig(level = logging.DEBUG)
    
    #   initialize the game window
    pygame.init()

    #   game clock and game screen
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((gb.SCREEN_WIDTH, gb.SCREEN_HEIGHT))

    #   game surface
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    #   draw the grid
    gb.draw_board(8, 8, surface)

    #   main game loop
    while True:
        clock.tick(25)

        #   update screen when ever there is an event
        screen.blit(surface, (0, 0))
        pygame.display.update()

        #   event handler
        for event in pygame.event.get():

            #   handles quit event
            if event.type == pygame.QUIT:
                pygame.quit()
                logging.debug("Quit game")
                sys.exit()


#   call main
if __name__ == "__main__":
    main()
