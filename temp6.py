from re import T
import pygame as pg
from random import randint
#dice loop fix
pg.init()
fps=60
is_both_players_on_same_square=0
clockk=pg.time.Clock()
window=pg.display.set_mode((1000,720))
pg.display.set_caption("Snakes and Ladders")
running = True
from time import sleep

ladder={4:25,21:39,29:74,43:76,63:80,71:89}
snake={30:7,47:15,56:19,73:51,82:42,92:75,98:55}

class img_loader:
    color=[180,180,195]
    def load(self):
        window.fill(self.color)
        background_image=pg.image.load("resources/snl_board.jpeg")
        image=pg.transform.smoothscale(background_image,[360,360])
        window.blit(image, (180, 100))
        title = self.font_40.render("SNAKE AND LADDERS", True, (3,152,60))
        window.blit(title,(230,50))
        whose_turn=self.font_40.render("TURN : "+turn_player, True, (150,60,150))
        window.blit(whose_turn,(290,520))
    font_40 = pg.font.Font(None,40)
    font_36 = pg.font.Font(None, 36)
    font_70 = pg.font.Font(None, 70)

class player:
    pos_x=188
    pos_y=428
    square_no=1
    path=""
    name=""
    def img_load(self):
        self.pre_image=pg.image.load(self.path)
        self.image=pg.transform.smoothscale(self.pre_image,[20,30])
        window.blit(self.image,[self.pos_x,self.pos_y])
    def move(self,square,player_2,img,if_not_ladder=60/36):
        self.target_square_no=square
        if ((self.target_square_no-1)//10)%2==0:
            self.target_posn=[188+36*((self.target_square_no-1)%10),428-36*((self.target_square_no-1)//10)]
        else:
            self.target_posn=[512-36*((self.target_square_no-1)%10),428-36*((self.target_square_no-1)//10)]
        self.current_x=self.pos_x
        self.current_y=self.pos_y
        self.change_of_x=(self.target_posn[0]-self.pos_x)/60*if_not_ladder
        self.change_of_y=(self.target_posn[1]-self.pos_y)/60*if_not_ladder
        while self.target_posn!=[self.pos_x,self.pos_y]:
            if self.pos_x!=self.target_posn[0]:
                self.current_x+=(self.change_of_x)
                self.pos_x=round(self.current_x)
                img.load()
                player_2.img_load()
                window.blit(self.image,[self.pos_x,self.pos_y])
                pg.display.flip()
            if self.pos_y!=self.target_posn[1]:
                self.current_y+=(self.change_of_y)
                self.pos_y=round(self.current_y)
                img.load()
                player_2.img_load()
                window.blit(self.image,[self.pos_x,self.pos_y])
                pg.display.flip()
        self.square_no=self.target_square_no
    def move_multiple(self,steps,player_2,img):
        for i in range(steps):
            if self.square_no==100:
                break
            self.move(self.square_no+1,player_2,img)
        if ladder.get(self.square_no,0) or snake.get(self.square_no,0):
            if ladder.get(self.square_no,0):
                self.target_square_no=ladder.get(self.square_no,0)-1
                self.move(self.target_square_no+1,player_2,pg_img_loader,1)
            else:
                self.target_square_no=snake.get(self.square_no,0)
                self.move(self.target_square_no,player_2,pg_img_loader,1)

class dice:
    dice_1=pg.transform.smoothscale(pg.image.load("resources/dice_01.png"),[100,100])
    dice_2=pg.transform.smoothscale(pg.image.load("resources/dice_02.png"),[100,100])
    dice_3=pg.transform.smoothscale(pg.image.load("resources/dice_03.png"),[100,100])
    dice_4=pg.transform.smoothscale(pg.image.load("resources/dice_04.png"),[100,100])
    dice_5=pg.transform.smoothscale(pg.image.load("resources/dice_05.png"),[100,100])
    dice_6=pg.transform.smoothscale(pg.image.load("resources/dice_06.png"),[100,100])
    dice_tuple=(dice_1,dice_2,dice_3,dice_4,dice_5,dice_6)
    is_rolling=False
    rolled=False

    def roller(self):
        self.is_rolling=True
        self.i,self.f=0.005,1/1.2
    
    
    
    
    
    
    
    def rolling(self,src):
        if self.is_rolling:
            src.load()
            p1.img_load()
            p2.img_load()
            self.x=725
            self.y=355
            window.blit(self.dice_tuple[randint(0,5)],(self.x,self.y))
            roll_text=pg_img_loader.font_36.render("  DICE", True, (50,50,50))
            window.blit(roll_text,(730,325))
            pg.display.flip()
            sleep(self.i)
            if self.i<=0.005:
                self.f*=1.2
            if self.i>=0.8 :
                self.f*=1/1.2
            if self.i>=0.8 and self.f==1/1.2:
                self.is_rolling=False
                self.rolled=True
                src.load()
                p1.img_load()
                p2.img_load()
                del self.i,self.f
                return self.roll(src)
            print(self.i,self.f)
            self.i*=self.f
            
    def roll(self,src):
        self.roll_no=randint(0,5)
        for self.i in range (3):
            self.x=725
            self.y=355
            window.blit(self.dice_tuple[self.roll_no],(self.x,self.y))
            roll_text=pg_img_loader.font_36.render("  DICE", True, (50,50,50))
            window.blit(roll_text,(730,325))
            pg.display.flip()
            sleep(0.8)
            src.load()
            p1.img_load()
            p2.img_load()
            roll_text=pg_img_loader.font_36.render("  DICE", True, (50,50,50))
            window.blit(roll_text,(730,325))
            pg.display.flip()
            sleep(0.8)
        del self.i
        return self.roll_no+1
    

p1=player()
p1.path="resources/player_1.png"
p1.name="name_1"
turn_player=p1.name
p2=player()
p2.path="resources/player_2.png"
p2.name="name_2"
dicee=dice()
p2.pos_x=188
p2.pos_y=428
button_x=730
button_y=140
button_height=100
button_width=100
button_color=(255,255,55)
is_clicked=False
pg_img_loader=img_loader()
is_both_players_on_same_square=1
p1.pos_y-=2
p2.pos_y+=2

r=True

while running:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running=False
    if r and randint(0,255)==255:
        r=False
        dicee.roller()
    dicee.rolling(pg_img_loader)
    # running=False
    pg.display.flip()
    clockk.tick(fps)