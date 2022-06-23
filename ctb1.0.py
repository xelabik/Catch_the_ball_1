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
runb_x1 = 600
runb_y1 = 450
runb_r1 = 50

runb_x2 = 600
runb_y2 = 450
runb_r2 = 50

step_x1 = 2
step_y1 = 2

step_x2 = 2
step_y2 = 2

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
                my_score += flag_runball1
                my_score += flag_runball2
                print("score", my_score)

        """ first running_ball """
        first_running_ball()
        """ second running_ball """
        second_running_ball()

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


def first_running_ball():
    """
    drawing ball that change his position
    coordinate: runb_x1, runb_y1.
    Radius: runb_r1
    """
    global runb_x1, runb_y1, runb_r1, step_x1, step_y1, color_flag, runball_color1

    if runb_x1 + runb_r1 > screen_length or runb_x1 - runb_r1 < 0:
        step_x1 = -step_x1
    if runb_y1 + runb_r1 > screen_width or runb_y1 - runb_r1 < 0:
        step_y1 = -step_y1
    runb_x1 += step_x1
    runb_y1 += step_y1
    circle(screen, runball_color, (runb_x1, runb_y1), runb_r1)


def second_running_ball():
    """
    drawing ball that change his position
    coordinate: runb_x, runb_y.
    Radius: runb_r
    """
    global runb_x2, runb_y2, runb_r2, step_x2, step_y2, color_flag, runball_color2

    if runb_x2 + runb_r2  > screen_length or runb_x2 - runb_r2 < 0:
        step_x2 = -step_x2
    if runb_y2 + runb_r2 > screen_width or runb_y2 - runb_r2 < 0:
        step_y2 = -step_y2
    runb_x2 -= step_x2
    runb_y2 -= step_y2
    circle(screen, runball_color, (runb_x2, runb_y2), runb_r2)


def click(event):
    """
    check if user hit the ball
    """
    global x_event, y_event, color_flag, \
           runb_x1, runb_y1, runb_r1, runball_color1, flag_runball1, step_x1, step_y1, \
           runb_x2, runb_y2, runb_r2, runball_color2, flag_runball2, step_x2, step_y2,\
           FPS

    x_event, y_event = event.pos

    """ cheking hit the first running ball """
    dtx1 = abs(x_event - runb_x1)
    dty1 = abs(y_event - runb_y1)
    click_try_runb1 = math.sqrt(dtx1 ** 2 + dty1 ** 2)
    flag_runball1 = 0
    if click_try_runb1 < runb_r1:
        flag_runball1 = 1
        runb_x1 = randint(50, 1150)
        runb_y1 = randint(50, 850)
        runb_r1 = randint(15, 49)
        runball_color1 = COLORS[randint(0, 5)]
        FPS += 10
        step_x1 += 1
        step_y1 += 1

    """ cheking hit the second running ball """
    dtx2 = abs(x_event - runb_x2)
    dty2 = abs(y_event - runb_y2)
    click_try_runb2 = math.sqrt(dtx2 ** 2 + dty2 ** 2)
    flag_runball2 = 0
    if click_try_runb2 < runb_r2:
        flag_runball2 = 1
        runb_x2 = randint(50, 1150)
        runb_y2 = randint(50, 850)
        runb_r2 = randint(15, 49)
        runball_color2 = COLORS[randint(0, 5)]
        FPS += 10
        step_x2 -= 1
        step_y2 -= 1
    return flag_runball1, flag_runball2


main()
