from Snake import Snake
from Board import Board
from SnakeBody import SnakeBody
from Food import Food
import pygame
import time
import numpy as np


def update_data_set(data_set, mov, snake, food):
    #initDataSet('DataSets.csv')
    new_row = np.array([0] * 66)
    new_row[((int(food.food_y / 10)-1) * 8) + ((int(food.food_x / 10)-1))] = 1
    for i in range(0, (len(snake) - 1)):
        if i == 0:
            new_row[((int(snake[i].y / 10)-1) * 8) + ((int(snake[i].x / 10)-1))] = 3
        else:
            new_row[((int(snake[i].y / 10)-1) * 8) + ((int(snake[i].x / 10)-1))] = 2

    new_row[65] = mov

    data_set = np.vstack([data_set, new_row])
    return data_set


def main():
    clock = pygame.time.Clock()
    window_width = 300
    window_height = 300
    display_width = 80
    display_height = 80


   
    game = True
    while game:
        score = 60
        game_display = Board(window_width, window_height)
        snake = Snake(20, 20, 3)
        food = Food(10, display_width, display_height, 10, snake)
        font = pygame.font.SysFont('Time New Roman, Arial', 20)
        text = font.render('Score: %d' % tuple([game_display.game_score]), False, Board.gold)
      
        x_change = 0
        y_change = 0
        first_time = True
        eat = True
        mov = 0
       
        data_sets = np.arange(66)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    game = False
                if event.type == pygame.KEYDOWN:
                    first_time = False
                    if event.key == pygame.K_LEFT:
                        if x_change != 10:
                            x_change = -10
                            y_change = 0
                            mov = 4
                    elif event.key == pygame.K_RIGHT:
                        if x_change != -10:
                            x_change = 10
                            y_change = 0
                            mov = 6
                    elif event.key == pygame.K_UP:
                        if y_change != 10:
                            x_change = 0
                            y_change = -10
                            mov = 8
                    elif event.key == pygame.K_DOWN:
                        if y_change != -10:
                            x_change = 0
                            y_change = 10
                            mov = 2

           
            if not first_time:
                data_sets = update_data_set(data_sets, mov, snake, food)
                snake.update(score)
            if score % 10 == 0 and eat:
                snake.append(SnakeBody(snake[len(snake) - 1].x, snake[len(snake) - 1].y))
                print(len(snake))
                eat = False
            snake.move_head(x_change, y_change)

            if (snake[0].x < food.food_x + 10 and snake[0].x >= food.food_x
                    and snake[0].y < food.food_y + 10 and snake[0].y >= food.food_y):
                score += 10
                game_display.game_score += 1
                food = Food(10, display_width, display_height, 10, snake)

                eat = True

            if snake.check_death(display_width, display_height):
                print("*****DEAD*****")
                restart = game_display.pop_exit_window(data_sets)
                if restart == True:
                    break

            game_display.clean()
            game_display.borders(display_height, display_width)
            pygame.draw.rect(game_display.GAME_display, Board.red,
                             (food.food_x, food.food_y, Snake.factor, Snake.factor))
            snake.draw(game_display.GAME_display)
            game_display.GAME_display.blit(text, (game_display.width - 50, 50))
            pygame.display.flip()
            time.sleep(0.280)
            clock.tick(60)


if __name__ == "__main__":
    main()