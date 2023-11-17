import pygame as pg


pg.init()
fps=60
is_both_players_on_same_square=0
clockk=pg.time.Clock()
window=pg.display.set_mode((1000,720))
pg.display.set_caption("Snakes and Ladders")
running = True

font_70 = pg.font.Font(None, 70)
font_36 = pg.font.Font("resources/test.ttf", 36)

class animations:
    i=0
    t=3
    blinking_i=0
    blinking_t=1
    blinking_q=0
    def blinking(self,font_engine,text,coords):
        if self.blinking_i>20:self.blinking_i,self.blinking_t=20,-1
        if self.blinking_i<0:self.blinking_i,self.blinking_t=0,1
        self.blinking_i+=self.blinking_t
        if self.blinking_t>0:self.blinking_q=0
        else:self.blinking_q=1
        print(self.blinking_q)
        window.blit(font_engine.render(text,True,[self.blinking_q*255]*3),coords)
    def breathing(self,font_engine,text,coords):
        if self.i>=255:self.t=-1*3
        if self.i<=0:self.t=+1*3
        self.i+=self.t
        window.blit(font_engine.render(text,True,[self.i]*3),coords)


animator=animations()
temp=pg.K_BACKSPACE
user_name=""

while running:
    for event in pg.event.get():  
        if event.type==pg.QUIT:
            running=False
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_BACKSPACE:
                if user_name!=[]:
                    user_name=user_name[:-1]
                continue
            user_name+=event.unicode
    

    window.fill((100,150,100))
    window.blit(font_36.render(user_name, True, (255,255,255)),(450,320))





    #animator.blinking(font_36,"Hello World",(450,320))
    pg.display.flip()

    clockk.tick(fps)




pg.quit()