import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def main():
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

        new_ball()
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


def new_ball():
    """
    drawing ball in random place,color and radius
    """

    global x, y, r
    x = randint(100, 700)
    y = randint(100, 500)
    r = randint(30, 50)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


def click(event):
    """
    check if user hit the ball
    """

    global x_event, y_event, flag
    x_event, y_event = event.pos
    print("ball xyr", x, y, r)
    print("my event pos", x_event, y_event)
    ptx = abs(x_event - x)
    pty = abs(y_event - y)
    print("ptxpty", ptx, pty)
    flag = 0
    if ptx < r and pty < r:
        print("goool")
        flag = 1
        print("funkscore", flag)
    return flag


main()

