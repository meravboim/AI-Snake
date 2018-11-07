import pygame
import numpy as np
import pandas as pd


def new_dat_f(dta_sts_matx):
    df = pd.DataFrame(dta_sts_matx)
    df.to_csv("DataSets.csv", header=None, index=None)


class Board:
    d_white = (250, 250, 250)
    blue_black = (50, 50, 50)
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    teal = (0, 128, 128)
    gold = (255, 215, 0)

    def __init__(self, width, height):
        pygame.init()
        pygame.display.set_caption('Snake')
        self.GAME_display = pygame.display.set_mode((width + 20, height + 20))
        self.clean()
        self.borders(width, height)
        self.game_score = 0
        self.width = width
        self.height = height

    def clean(self):
        self.GAME_display.fill(Board.white)
        pygame.display.update()

    def borders(self, height, width):
        # top line
        pygame.draw.rect(self.GAME_display, Board.black, [0, 0, height + 20, 10])
        # bottom line
        pygame.draw.rect(self.GAME_display, Board.black, [0, width + 10, height + 20, 10])
        # left line
        pygame.draw.rect(self.GAME_display, Board.black, [0, 0, 10, height + 20])
        # right line
        pygame.draw.rect(self.GAME_display, Board.black, [height + 10, 0, 10, width + 20])
        pygame.display.update()

    def close(self):
        print("preparing to exit...")
        pygame.quit()
        quit()

    def pop_exit_window(self, datsts):
        #       pygame.draw.rect(self.GAME_display, Board.white, (10,80,20,20), 100)
        pygame.font.init()  # you have to call this at the start,

        myfont = pygame.font.SysFont('Comic Sans MS', 20)
        text = myfont.render('To restart press C, Exit press X', False, (50, 50, 50))
        text2 = myfont.render('Your final score is: %d ' % tuple([self.game_score]), False, Board.red)
        self.GAME_display.blit(text, (10, self.height / 2 + 50))
        self.GAME_display.blit(text2, (self.width/2 - 60, self.height/2))
        pygame.display.update()

        new_dat_f(datsts)

        flag = True
        while flag:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    # quit()
                    flag = False
                    return False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        pygame.quit()
                        # quit()
                        flag = False
                        return False
                    elif event.key == pygame.K_c:
                        self.clean()
                        return True
