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

rect_x1 = -1200
rect_y1 = randint(100, 800)

rect_x2 = randint(100, 1100)
rect_y2 = -1200
OUTPUT_RESULTS_FILE = "ScoreTable.txt"


def main():
    global rect_x1, rect_y2, runball_color1, runball_color2, FPS
    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False
    score = 0
    runball_color1 = COLORS[randint(0, 5)]
    runball_color2 = COLORS[randint(0, 5)]

    while not finished:
        clock.tick(FPS)
        """ mouse click and score"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
                save_score(score, file_to_save=OUTPUT_RESULTS_FILE)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click(event)
                score += flag_runball1
                score += flag_runball2
                score += flag_rectangles_cross1
                score += flag_rectangles_cross2
                if flag_rectangles_cross1 or flag_rectangles_cross2:
                    rect_x1 = -1200
                    rect_y2 = -1200
                print("score", score, "FPS", FPS)

        """ first running_ball """
        first_running_ball()

        """ second running_ball """
        second_running_ball()

        """rectangles_cross"""
        if FPS % 200 == 0:
            rectangles_cross()

        pygame.display.update()
        screen.fill(BLACK)

    pygame.quit()


def save_score(score: int, file_to_save: str) -> None:
    """
    Save thr given score.

    Args:
        score (int) : the score to save
        file_to_save (str): the file to save the score
    """
    username = input("insert your name")
    print(f"{username} Game Over you have {score} points")
    with open(file_to_save, "a") as file:
        file.write(username + "-" + str(score) + '\n')


def first_running_ball():
    """
    drawing ball that change his position
    coordinate: runb_x1, runb_y1.
    Radius: runb_r1
    """
    global runb_x1, runb_y1, runb_r1, step_x1, step_y1

    if runb_x1 + runb_r1 > screen_length or runb_x1 - runb_r1 < 0:
        step_x1 = -step_x1
    if runb_y1 + runb_r1 > screen_width or runb_y1 - runb_r1 < 0:
        step_y1 = -step_y1
    runb_x1 += step_x1
    runb_y1 += step_y1
    circle(screen, runball_color1, (runb_x1, runb_y1), runb_r1)


def second_running_ball():
    """
    drawing ball that change his position
    coordinate: runb_x, runb_y.
    Radius: runb_r
    """
    global runb_x2, runb_y2, runb_r2, step_x2, step_y2

    if runb_x2 + runb_r2 > screen_length or runb_x2 - runb_r2 < 0:
        step_x2 = -step_x2
    if runb_y2 + runb_r2 > screen_width or runb_y2 - runb_r2 < 0:
        step_y2 = -step_y2
    runb_x2 -= step_x2
    runb_y2 -= step_y2
    circle(screen, runball_color2, (runb_x2, runb_y2), runb_r2)


def rectangles_cross():
    """
    drawing two rectangles
    firs rectangle coordinate: rect_x1, rect_y1
    second rectangle coordinate: rect_x2, rect_y2

    """
    global rect_x2, rect_y2, rect_x1
    print("eeeeeee")
    """horizontal rectangle !!"""
    rect(screen, (255, 255, 255), (rect_x1, rect_y1, 400, 50))
    rect_x1 += 4

    """vertical rectangle """
    rect(screen, (255, 255, 255), (rect_x2, rect_y2, 50, 400))
    rect_y2 += 4
    print(rect_x1, rect_y1)
    print(rect_x2, rect_y2)


def click(event):
    """
    check if user hit the ball
    """
    global x_event, y_event, \
        runb_x1, runb_y1, runb_r1, runball_color1, flag_runball1, step_x1, step_y1, \
        runb_x2, runb_y2, runb_r2, runball_color2, flag_runball2, step_x2, step_y2, \
        FPS, flag_rectangles_cross1, flag_rectangles_cross2

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
        runb_r1 = randint(25, 49)
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
        runb_r2 = randint(25, 49)
        runball_color2 = COLORS[randint(0, 5)]
        FPS += 10
        step_x2 -= 1
        step_y2 -= 1

    """ cheking hit the rectangles_cross """
    flag_rectangles_cross1 = 0
    if rect_x1 < x_event < rect_x1 + 400 and \
       rect_y1 < y_event < rect_y1 + 50:
        FPS -= 100
        flag_rectangles_cross1 = 1

    flag_rectangles_cross2 = 0
    if rect_x2 < x_event < rect_x2 + 50 and \
       rect_y2 < y_event < rect_y2 + 400:
        FPS -= 100
        flag_rectangles_cross2 = 1

    print("step_x1 step_y1", step_x1, step_y1)
    print("step_x2 step_y2", step_x2, step_y2)
    return flag_runball1, flag_runball2,\
        flag_rectangles_cross1, flag_rectangles_cross2


main()
