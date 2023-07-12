import pygame as pg
from time import sleep
from random import randint
pg.init()
fps=60
window=pg.display.set_mode((720,720))
pg.display.set_caption("Snakes and Ladders")
running = True
class img_loader:
    color=[180,180,195]
    def load(self):
        window.fill(self.color)
        background_image=pg.image.load("resources/snl_board.jpeg")
        image=pg.transform.smoothscale(background_image,[360,360])
        window.blit(image, (180, 100))
    def font():
        font = pg.font.Font(None, 36)
class player:
    pos_x=185
    pos_y=425
    square_no=1
    def img_load(self,path):
        self.pre_image=pg.image.load(path)
        self.image=pg.transform.smoothscale(self.pre_image,[20,30])
        window.blit(self.image,[self.pos_x,self.pos_y])
    def move(self,p2,img):
        for self.i in range(36):
            if self.square_no%10==0:
                self.pos_y-=1
                img.load()
                p2.img_load("resources/player_2.png")
                window.blit(self.image,[self.pos_x,self.pos_y])
                pg.display.flip()
            elif int(self.square_no/10)%2==1:
                self.pos_x-=1
                img.load()
                p2.img_load("resources/player_2.png")
                window.blit(self.image,[self.pos_x,self.pos_y])
                pg.display.flip()                
            else:
                self.pos_x+=1
                img.load()
                p2.img_load("resources/player_2.png")
                window.blit(self.image,[self.pos_x,self.pos_y])
                pg.display.flip()
        self.square_no+=1
        del self.i
    def move_multiple(self,steps):
        for self.i in range(steps):
            self.move(p2,pg_img_loader)
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
        return self.roll(src)
    def roll(self,src):
        self.roll_no=randint(0,5)
        for self.i in range (3):
            src.load()
            pg.display.flip()
            sleep(1)
            self.x=20
            self.y=20
            window.blit(self.dice_tuple[self.roll_no],(self.x,self.y))
            pg.display.flip()
            sleep(1)
        del self.i
        return self.roll_no
p1=player()
p2=player()
dice=dice()
p2.pos_x=188
p2.pos_y=428
pg_img_loader=img_loader()
while running:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running=False
        if event.type == pg.MOUSEBUTTONDOWN:#temp , change l8r
            pg_img_loader.load()
            p1.img_load("resources/player_1.png")
            p1.move_multiple(dice.rolling(pg_img_loader)+1)
            p2.img_load("resources/player_2.png")
        
pg.quit()