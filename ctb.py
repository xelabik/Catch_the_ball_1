import pygame
import math
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1

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
runb_x = 600
runb_y = 450
runb_r = 50
step_x = 33
step_y = 33


def main():
    global runb_x, runb_y, runb_r, step_x, step_y
    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False
    my_score = 0

    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
                score_save(my_score)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print('Cycle start!')
                click(event)
                my_score += flag
                print("score", my_score)

        new_statick_ball()

        running_ball(runb_x, runb_y, runb_r)
        if runb_x+runb_r > screen_length or runb_x-runb_r < 0:
            step_x = -step_x
        if runb_y + runb_r > screen_width or runb_y - runb_r < 0:
            step_y = -step_y
        runb_x += step_x
        runb_y += step_y

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


def running_ball(runb_x, runb_y, runb_r):
    """
    drawing ball that change your color and position
    coordinate: runb_x, runb_y.
    Radius: runb_r
    """
    color = COLORS[randint(0, 5)]
    circle(screen, color, (runb_x, runb_y), runb_r)


def click(event):
    """
    check if user hit the ball
    """

    global x_event, y_event, flag
    x_event, y_event = event.pos
    #  print("ball xyr", x, y, r)
    #  print("my event pos", x_event, y_event)
    ptx = abs(x_event - x)
    pty = abs(y_event - y)
    #  print("ptxpty", ptx, pty)
    flag = 0
    click_try = math.sqrt(ptx**2 + pty**2)
    print("click_try", click_try)
    if click_try < r:
        print("goool-statick")
        flag = 1
        print("funkscore", flag)
    return flag


main()

