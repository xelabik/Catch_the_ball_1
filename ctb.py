import math
from random import randint
from typing import Tuple

import pygame
from pygame.draw import *

pygame.init()

FPS = 1

screen_length: int = 1200
screen_width: int = 900
screen = pygame.display.set_mode((screen_length, screen_width))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
""" running ball parameters"""
runb_x: int = 600
runb_y: int = 450
runb_r: int = 50
step_x: int = 40
step_y: int = 40

OUTPUT_RESULTS_FILE = "ScoreTable.txt"

def main():
    # global runb_x, runb_y, runb_r, step_x, step_y
    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False
    current_score = 0

    while not finished:
        clock.tick(FPS)
        """ mouse click and score"""
        for event in pygame.event.get():
            print(type(event))
            if event.type == pygame.QUIT:
                finished = True
                save_score(score=current_score, file_to_save=OUTPUT_RESULTS_FILE)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print('Cycle start!')
                on_click(event)
                current_score += flag_statball
                current_score += flag_runball
                print("score", current_score)

        """ statick ball"""
        new_statick_ball()

        """ running_ball"""
        running_ball()

        pygame.display.update()
        screen.fill(BLACK)

    pygame.quit()


def save_score(score: int, file_to_save: str) -> None:
    """
    Save the given score.

    Args:
        score (int): the score to save
        file_to_save (str): the file to save the score
    """
    username = input("insert your name")
    print(f"{username} Game Over you have {score} points")
    with open(file_to_save, "a") as file:
        file.write(username + "-" + str(score) + '\n')


def new_statick_ball():
    """
    drawing ball in random place,color and radius
    """
    global x, y, r
    x = randint(100, 700)
    y = randint(100, 500)
    r = randint(30, 50)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


def running_ball():
    """
    drawing ball that change his position
    coordinate: runb_x, runb_y.
    Radius: runb_r
    """
    global runb_x, runb_y, runb_r, step_x, step_y
    if runb_x + runb_r > screen_length or runb_x - runb_r < 0:
        step_x = -step_x
    if runb_y + runb_r > screen_width or runb_y - runb_r < 0:
        step_y = -step_y
    runb_x += step_x
    runb_y += step_y
    circle(screen, (50, 50, 50), (runb_x, runb_y), runb_r)


def on_click(event: pygame.event.Event) -> Tuple[bool]:
    """
    _summary_

    Args:
        event (pygame.event.Event): _description_

    Returns:
        Tuple[bool]: _description_
    """

    global x_event, y_event, flag_statball, flag_runball
    x_event, y_event = event.pos

    ptx = abs(x_event - x)
    pty = abs(y_event - y)
    click_try = math.sqrt(ptx ** 2 + pty ** 2)
    flag_statball = 0
    if click_try < r:
        flag_statball = 1
    dtx = abs(x_event - runb_x)
    dty = abs(y_event - runb_y)
    click_try_runb = math.sqrt(dtx ** 2 + dty ** 2)
    flag_runball = 0
    if click_try_runb < runb_r:
        flag_runball = 2
    print("statick run", flag_statball, flag_runball)
    return flag_statball, flag_runball

if __name__ == "__main__":
    main()

