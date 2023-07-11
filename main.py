import pygame as pg
pg.init()
fps=60
window=pg.display.set_mode((720,720))
pg.display.set_caption("Snakes and Ladders")
window.fill((180,180,195))
running = True
class img_loader:
    def load(self):
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
        for self.i in range(int(360/fps)):
            if self.square_no%10==0:
                self.pos_y-=1
                img.load()
                p2.img_load("resources/player_2.png")
                window.blit(self.image,[self.pos_x,self.pos_y])
            else:
                self.pos_x+=1
                img.load()
                p2.img_load("resources/player_2.png")
                window.blit(self.image,[self.pos_x,self.pos_y])
            self.square_no+=1
        del self.i
    def move_multiple(self,steps):
        for self.i in range(steps):
            self.move(p2,pg_img_loader)
p1=player()
p2=player()
p2.pos_x=188
p2.pos_y=428
pg_img_loader=img_loader()
while running:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running=False
        pg_img_loader.load()
        p1.img_load("resources/player_1.png")
        p1.move_multiple(6)
        p2.img_load("resources/player_2.png")
        pg.display.flip()
pg.quit()