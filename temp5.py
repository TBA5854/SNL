from time import sleep
import pygame as pg

pg.init()
fps=60
clockk=pg.time.Clock()
window=pg.display.set_mode((1000,720))
pg.display.set_caption("Snakes and Ladders")
running = True

class animations:
    i=0
    m=0
    t=3
    lbl_i=0
    lbl_t=0
    faded=False
    faded_start=False
    faded_t=0
    blinking_i=0
    blinking_t=1
    blinking_q=0
    def blinking(self,font_engine,text,r,g,b,coords):
        if self.blinking_i>40:self.blinking_i,self.blinking_t=40,-1
        if self.blinking_i<0:self.blinking_i,self.blinking_t=0,1
        self.blinking_i+=self.blinking_t
        if self.blinking_t>0:window.blit(font_engine.render(text,True,[r,g,b]),coords)
        pg.display.flip()
    def breathing(self,font_engine,text,r,g,b,coords):
        if max(r,g,b)>=252:
            self.t=-1*4
        if min(r,g,b)<=4:
            self.t=+1*4
        r+=self.t
        g+=self.t
        b+=self.t
        print(r,g,b,self.t)
        window.blit(font_engine.render(text,True,[r,g,b]),coords)
        return r,g,b
    def fade_in(self,font_engine,text,r,g,b,coords):
        if self.faded_start and self.faded_t>0:
            self.faded=True
            window.blit(font_engine.render(text,True,[r,g,b]),coords)
            return r,g,b
        if self.m<max(r,g,b):self.m=max(r,g,b)
        if max(r,g,b)>=252:
            self.faded_t=-1*4
        if min(r,g,b)<=4:
            self.faded_t=+1*4
        r+=self.faded_t
        g+=self.faded_t
        b+=self.faded_t
        print(r,g,b,self.faded_t)
        if self.faded_start or self.faded_t>0:
            window.blit(font_engine.render(text,True,[r,g,b]),coords)
            if self.m==max(r,g,b):
                self.faded_start=True
        # pg.display.flip()
        return r,g,b
    def lbl(self,font_engine,text,r,g,b,coords):
        if self.lbl_t==90:
            if self.lbl_i != len(text):
                self.lbl_i+=1
            self.lbl_t=0
        else:self.lbl_t+=1
        window.blit(font_engine.render(text[:self.lbl_i],True,[r,g,b]),coords)
        # pg.display.flip()
window.fill((0,0,0))
font_70 = pg.font.Font(None, 70)
font_36 = pg.font.Font("resources/test.ttf", 36)

animator=animations()
r=g=b=255
title="SNL"
temp=temp1=1
while running:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running=False
        if event.type==pg.KEYDOWN and event.key==pg.K_RETURN:
            running=False

    # sleep(0.1)
    window.fill((0,0,0))

    animator.lbl(font_70,title,255,255,255,(425,100))
    if animator.lbl_i==len(title):
        if temp:
            temp=0
            pg.display.flip()
            sleep(1)
        r,g,b=animator.fade_in(font_36,"By TBA5854",r,g,b,(500,150))
        if animator.faded:
            if temp1:
                temp1=0
                pg.display.flip()
                sleep(0.25)
            animator.blinking(font_36,"PRESS ENTER",255,255,255,(350,450))
    pg.display.flip()
    clockk.tick(fps)