import pygame as pg
from time import sleep
from random import randint
choice=0#int(input("Do you want to play 2 player or player vs computer : (0 for computer and 1 for 2 player)\n>>"))
while choice not in [0,1]:
    print("INVALID INPUT \n")
    choice=int(input("Do you want to play 2 player or player vs computer : (0 for computer and 1 for 2 player)\n>>"))
if choice:
    name_1=input("Enter Player 1 Name \n>>")
    name_2=input("Enter Player 2 Name \n>>")
else:
    name_1="TBA"#input("Enter Player 1 Name \n>>")
    name_2="Computer"
ladder={4:25,21:39,29:74,43:76,63:80,71:89}
snake={30:7,47:15,56:19,73:51,82:42,92:75,98:55}
pg.init()
fps=60
is_both_players_on_same_square=0
clockk=pg.time.Clock()
window=pg.display.set_mode((1000,720))
pg.display.set_caption("Snakes and Ladders")
running = True
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
        self.button_rect=pg.draw.rect(window ,button_color, (button_x, button_y, button_width, button_height))
        roll_button=self.font_36.render("ROLL", True, (0,0,0))
        window.blit(roll_button,(750,178))
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
        for i in range(steps-1):
            if self.square_no==100:
                break
            self.move(self.square_no+1,player_2,pg_img_loader)
        if ladder.get(self.square_no,0) or snake.get(self.square_no,0):
            if ladder.get(self.square_no,0):
                self.target_square_no=ladder.get(self.square_no,0)-1
                self.move(self.target_square_no+1,player_2,pg_img_loader,1)
            else:
                self.target_square_no=snake.get(self.square_no,0)-1
                self.move(self.target_square_no,player_2,pg_img_loader,1)
def win():
    pg.draw.rect(window ,(205,205,205), (0, 120, 1000,400))
    if p1.square_no>=100:
        win_text = p1.name+" Wins !!!"
    elif p2.square_no>=100:
        win_text = p2.name+" Wins !!!"
    text_surface2 = img_loader.font_70.render(win_text, True, (randint(0,255), randint(0,255), randint(0,255)))
    window.blit(text_surface2,(270,290))
    pg.display.flip()
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
            p1.img_load()
            p2.img_load()
            self.x=725
            self.y=355
            window.blit(self.dice_tuple[randint(0,5)],(self.x,self.y))
            roll_text=pg_img_loader.font_36.render("   DICE", True, (50,50,50))
            window.blit(roll_text,(730,325))
            pg.display.flip()
            #sleep(0.5)
        del self.i
        return self.roll(src)
    def roll(self,src):
        self.roll_no=randint(0,5)
        for self.i in range (3):
            src.load()
            p1.img_load()
            p2.img_load()
            pg.display.flip()
            #sleep(1)
            self.x=20
            self.y=20
            window.blit(self.dice_tuple[self.roll_no],(self.x,self.y))
            pg.display.flip()
            #sleep(1)
        del self.i
        return self.roll_no+1
class interchange_2_player:
    turn=1
    def swapper(self,p1,p2):
        if self.turn:
            p1.move_multiple(dicee.rolling(pg_img_loader)+1,p2,pg_img_loader)
            self.turn-=1
            turn_player=p2.name
        else:
            p2.move_multiple(dicee.rolling(pg_img_loader)+1,p1,pg_img_loader)
            self.turn+=1
            turn_player=p1.name
        if p1.square_no>p2.square_no:
            pg_img_loader.color=[180,180,247]
        elif p1.square_no<p2.square_no:
            pg_img_loader.color=[247,180,180]
        elif p1.square_no==p2.square_no:
            pg_img_loader.color=[180,180,180]
class interchange_computer:
    def swapper(self,p1,p2):
        if p1.square_no>p2.square_no:
            pg_img_loader.color=[180,180,247]
        elif p1.square_no<p2.square_no:
            pg_img_loader.color=[247,180,180]
        elif p1.square_no==p2.square_no:
            pg_img_loader.color=[180,180,180]
        p1.move_multiple(dicee.rolling(pg_img_loader),p2,pg_img_loader)
        print(dicee.roll_no)
        sleep(2)
        if p1.square_no>p2.square_no:
            pg_img_loader.color=[180,180,247]
        elif p1.square_no<p2.square_no:
            pg_img_loader.color=[247,180,180]
        elif p1.square_no==p2.square_no:
            pg_img_loader.color=[180,180,180]
        p2.move_multiple(dicee.rolling(pg_img_loader)+1,p1,pg_img_loader)
        print(dicee.roll_no)
if choice:
    player_change=interchange_2_player()
else:
    player_change=interchange_computer()
p1=player()
p1.path="resources/player_1.png"
p1.name=name_1
turn_player=p1.name
p2=player()
p2.path="resources/player_2.png"
p2.name=name_2
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
while running:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running=False
    if(p1.square_no>=100):
        win()
        #sleep(1)
        continue
    if(p2.square_no>=100):
        win()
        #sleep(1)
        continue
    pg_img_loader.load()
    p1.img_load()
    p2.img_load()
    pg.display.flip()
    if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
        if pg_img_loader.button_rect.collidepoint(event.pos) and not is_clicked:
            is_clicked = True
            if is_both_players_on_same_square:
                p2.pos_y-=2
                p1.pos_y+=2
                is_both_players_on_same_square=0
            print("Button clicked!")
            print(p1.pos_x,p1.pos_y,p1.square_no)
            player_change.swapper(p1,p2)
            if p1.square_no==p2.square_no:
                is_both_players_on_same_square=1
                p1.pos_y-=2
                p2.pos_y+=2
    if event.type == pg.MOUSEBUTTONUP and event.button == 1:
        is_clicked = False
        pass
    clockk.tick(fps)
pg.quit()
# To undo 
# sleep\
# prob:
# roll not consistent
# turn name nit changing
# display should update as soon as either players tutn ends and update color instead of updating after some action by user
# roll button should not appear when other computer playing or animating time 