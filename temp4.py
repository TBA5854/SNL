import pygame as pg
from random import randint

pg.init()
fps=60
is_both_players_on_same_square=0
clockk=pg.time.Clock()
window=pg.display.set_mode((1000,720))
pg.display.set_caption("Snakes and Ladders")
running = True
from time import sleep
quit_box=pg.draw.rect(window,(255, 141, 141),(100,100,250,75))
play_again=pg.draw.rect(window,(137, 255, 159),(100,200,250,75))
def conf():
    no=pg.draw.rect(window,(255, 141, 141),(200,450,250,75))
    yes=pg.draw.rect(window,(137, 255, 159),(500,450,250,75))
    running1=True
    while running1:
        for event in pg.event.get():
            if event.type==pg.QUIT:
                running=False
            if event.type==pg.MOUSEBUTTONDOWN:
                if event.button==1:
                    mouse_pos=pg.mouse.get_pos()
                    if no.collidepoint(mouse_pos):
                        print("No")
                        running1=False
                        return False
                    if yes.collidepoint(mouse_pos):
                        print("Yes")
                        return True
                        running1=False
        pg.draw.rect(window,(128,128,128,128),(0,0,1000,720))
        no=pg.draw.rect(window,(255, 141, 141),(200,450,250,75))
        yes=pg.draw.rect(window,(137, 255, 159),(500,450,250,75))
        pg.display.flip()

while running:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running=False
        if event.type==pg.MOUSEBUTTONDOWN:
            if event.button==1:
                mouse_pos=pg.mouse.get_pos()
                if quit_box.collidepoint(mouse_pos):
                    if conf():
                        pg.display.flip()#cqll loader here
                        print("Quit")
                        running=False
                if play_again.collidepoint(mouse_pos):
                    if conf():
                        pg.display.flip()#call loader here
                        print("Play Again")
                    # pos_x=188
                    # pos_y=428
                    # square_no=1
    clockk.tick(fps)
    quit_box=pg.draw.rect(window,(255, 141, 141),(100,100,250,75))
    play_again=pg.draw.rect(window,(137, 255, 159),(100,200,250,75))
    pg.display.flip()