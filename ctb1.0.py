import pygame
import math
from pygame.draw import *
from random import randint
pygame.init()

FPS = 60

screen_length = 1200
screen_width = 900
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
runb_x = 600
runb_y = 450
runb_r = 50
step_x = 2
step_y = 2


def main():
    global runball_color, FPS
    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False
    my_score = 0
    runball_color = COLORS[randint(0, 5)]

    while not finished:
        clock.tick(FPS)
        """ mouse click and score"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
                score_save(my_score)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print('Cycle start!')
                click(event)
                my_score += flag_runball
                print("score", my_score)

        """ statick ball"""

        """ running_ball"""
        running_ball()

        pygame.display.update()
        screen.fill(BLACK)

    pygame.quit()


def score_save(my_score):
    """
     give user name and save his name and score to ScoreTable.txt
    """
    username = input("insert your name")
    print(username, "Game Over you have ", my_score, "points", )
    outputfile = "ScoreTable.txt"
    myfile = open(outputfile, mode="a")
    myfile.write(username + "-" + str(my_score) + '\n')
    myfile.close()


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
    global runb_x, runb_y, runb_r, step_x, step_y, color_flag, runball_color

    if runb_x + runb_r > screen_length or runb_x - runb_r < 0:
        step_x = -step_x
    if runb_y + runb_r > screen_width or runb_y - runb_r < 0:
        step_y = -step_y
    runb_x += step_x
    runb_y += step_y
    circle(screen, runball_color, (runb_x, runb_y), runb_r)


def click(event):
    """
    check if user hit the ball
    """

    global x_event, y_event, flag_runball, color_flag, runb_x, runb_y, runb_r,\
           runball_color, FPS, step_x, step_y

    x_event, y_event = event.pos

    """ cheking hit the running ball """
    dtx = abs(x_event - runb_x)
    dty = abs(y_event - runb_y)
    click_try_runb = math.sqrt(dtx ** 2 + dty ** 2)
    flag_runball = 0
    if click_try_runb < runb_r:
        flag_runball = 1
        color_flag = 1
        runb_x = randint(50, 1150)
        runb_y = randint(50, 850)
        runb_r = randint(15, 49)
        runball_color = COLORS[randint(0, 5)]
        FPS += 10
        step_x += 1
        step_y += 1
        print("FPS", FPS, step_x, step_y)
    print(" run_flag ", flag_runball)
    return flag_runball


main()

