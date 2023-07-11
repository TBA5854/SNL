import pygame as pg
pg.init()
window=pg.display.set_mode((720,720))
class player:
    pos_x=0
    pos_y=0
    square_no:1
    def img_load(self,path):
        self.pre_image=pg.image.load(path)
        self.image=pg.transform.smoothscale(self.pre_image,[30,30])
        window.blit(self.image,[self.pos_x,self.pos_y])
    def move(self,fps):
        for self.i in range(360/fps):
            if self.square_no%10==0:
                self.pos_y+=1
                window.blit(self.image,[self.pos_x,self.pos_y])
            else:
                self.pos_x+=1
                window.blit(self.image,[self.pos_x,self.pos_y])
            self.square_no+=1
        del self.i
    def move_multiple(self,steps):
        for self.i in range(steps):
            self.move()
    