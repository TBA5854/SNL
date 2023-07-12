import pygame as pg
from time import sleep
from random import randint
pg.init()
window=pg.display.set_mode((720,720))
pg.display.set_caption("Snakes and Ladders")
running = True
class img_loader:
    def load(self):
        window.fill(self.color)
        background_image=pg.image.load("resources/snl_board.jpeg")
        image=pg.transform.smoothscale(background_image,[360,360])
        window.blit(image, (180, 100))
    color=[180,180,195]
    def font():
        font = pg.font.Font(None, 36)
class dice:
    dice_1=pg.transform.smoothscale(pg.image.load("resources/dice_01.png"),[100,100])
    dice_2=pg.transform.smoothscale(pg.image.load("resources/dice_02.png"),[100,100])
    dice_3=pg.transform.smoothscale(pg.image.load("resources/dice_03.png"),[100,100])
    dice_4=pg.transform.smoothscale(pg.image.load("resources/dice_04.png"),[100,100])
    dice_5=pg.transform.smoothscale(pg.image.load("resources/dice_05.png"),[100,100])
    dice_6=pg.transform.smoothscale(pg.image.load("resources/dice_06.png"),[100,100])
    dice_tuple=(dice_1,dice_2,dice_3,dice_4,dice_5,dice_6)
    def rolling(self,src):
        for self.i in range(6):
            src.load()
            self.x=20
            self.y=20
            window.blit(self.dice_tuple[randint(0,5)],(self.x,self.y))
            pg.display.flip()
            sleep(0.5)
        del self.i
        sleep(1)
        self.roll(src)
    def roll(self,src):
        self.roll=randint(0,5)
        for self.i in range (3):
            src.load()
            pg.display.flip()
            sleep(1)
            self.x=20
            self.y=20
            window.blit(self.dice_tuple[self.roll],(self.x,self.y))
            pg.display.flip()
            sleep(1)
        del self.i
        return self.roll
pg_img_loader=img_loader()
dice1=dice()
while running:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running=False
        pg_img_loader.load()
        pg.display.flip()
        if event.type == pg.MOUSEBUTTONDOWN:
            dice1.rolling(pg_img_loader)
        pg.display.update()
pg.quit()