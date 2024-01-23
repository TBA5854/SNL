import pygame as pg
from time import sleep
from random import randint


choice=int(input("Do you want to play 2 player or player vs computer : (0 for computer and 1 for 2 player)\n>>"))
while choice not in [0,1]:
    print("\nINVALID INPUT!!!\n")    
    choice=int(input("Do you want to play 2 player or player vs computer : (0 for computer and 1 for 2 player)\n>>"))
""" if choice:
    name_1=input("Enter Player 1 Name \n>>")
    name_2=input("Enter Player 2 Name \n>>")
else:
    name_1=input("Enter Player 1 Name \n>>")
    name_2="Computer" """
ladder={4:25,21:39,29:74,43:76,63:80,71:89}
snake={30:7,47:15,56:19,73:51,82:42,92:75,98:55}
pg.init()
fps=60
is_both_players_on_same_square=0
clockk=pg.time.Clock()
window=pg.display.set_mode((1000,720))
pg.display.set_caption("Snakes and Ladders")
running = True
is_started=False

class loading_screen:
    r=g=b=255
    title="SNL"
    temp=temp1=1
    def load(self):
        global is_started
        is_started=True
        animator.lbl(font_70,self.title,255,255,255,(425,100))
        if animator.lbl_i==len(self.title):
            if self.temp:
                self.temp=0
                pg.display.flip()
                sleep(1)
            self.r,self.g,self.b=animator.fade_in(font_36,"By TBA5854",self.r,self.g,self.b,(500,150))
            if animator.faded:
                if self.temp1:
                    self.temp1=0
                    pg.display.flip()
                    sleep(0.25)
                animator.blinking(font_36,"PRESS ENTER",255,255,255,(350,450))

loader=loading_screen()

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
                        running1=False
                        return False
                    if yes.collidepoint(mouse_pos):
                        return True
        
        pg.draw.rect(window,(181, 82, 82),(0,0,1000,720))
        no=pg.draw.rect(window,(255, 141, 141),(200,450,250,75))
        yes=pg.draw.rect(window,(137, 255, 159),(500,450,250,75))
        window.blit(pg.font.Font(None, 70).render("CONFIRM ?", True, (255, 243, 213)), (350,150))
        window.blit(pg.font.Font(None,50).render("YES", True, (55,139,99)), (593,473))
        window.blit(pg.font.Font(None,50).render("NO  ", True, (255,0,61)), (300,472))
        pg.display.flip()

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
    def breathing(self,font_engine,text,r,g,b,coords):
        if max(r,g,b)>=252:
            self.t=-1*4
        if min(r,g,b)<=4:
            self.t=+1*4
        r+=self.t
        g+=self.t
        b+=self.t
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
        if self.faded_start or self.faded_t>0:
            window.blit(font_engine.render(text,True,[r,g,b]),coords)
            if self.m==max(r,g,b):
                self.faded_start=True
        return r,g,b
    def lbl(self,font_engine,text,r,g,b,coords):
        if self.lbl_t==90:
            if self.lbl_i != len(text):
                self.lbl_i+=1
            self.lbl_t=0
        else:self.lbl_t+=1
        window.blit(font_engine.render(text[:self.lbl_i],True,[r,g,b]),coords)
font_70 = pg.font.Font(None, 70)
font_36 = pg.font.Font("resources/test.ttf", 36)
animator=animations()
player_turn_color=[192, 192, 192]
class img_loader:
    color=[97,97,97]
    def load(self):
        window.fill(self.color)
        background_image=pg.image.load("resources/snl_board.jpeg")
        image=pg.transform.smoothscale(background_image,[360,360])
        window.blit(image, (180, 100))
        title = self.font_40.render("SNAKE AND LADDERS", True, (237, 224, 200))
        window.blit(title,(230,50))
        whose_turn=self.font_40.render("TURN : "+turn_player, True, player_turn_color)
        window.blit(whose_turn,(290,520))
    font_40 = pg.font.Font(None,40)
    font_36 = pg.font.Font(None, 36)
    font_70 = pg.font.Font(None, 70)
    def roll_button(self):
            self.button_rect=pg.draw.rect(window ,button_color, (button_x, button_y, button_width, button_height))
            pg.draw.rect(window,pg_img_loader.color,(730,140,18,18))
            pg.draw.circle(window,button_color,(730+18,140+18),18)#1
            pg.draw.rect(window,pg_img_loader.color,(830-18,140,18,18))
            pg.draw.circle(window,button_color,(830-18,140+18),18)#2
            pg.draw.rect(window,pg_img_loader.color,(730,240-18,18,18))
            pg.draw.circle(window,button_color,(730+18,240-18),18)#3
            pg.draw.rect(window,pg_img_loader.color,(830-18,240-18,18,18))
            pg.draw.circle(window,button_color,(830-18,240-18),18)#4
            animator.blinking(pg_img_loader.font_36,"ROLL",0,0,0,(750,178))
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
def win():
    pg.draw.rect(window ,(205,205,205), (0, 120, 1000,400))
    if p1.square_no>=100:
        win_text = p1.name+" Wins !!!"
    else:
        win_text = p2.name+" Wins !!!"
    text_surface2 = img_loader.font_70.render(win_text, True, (randint(0,255), randint(0,255), randint(0,255)))
    window.blit(text_surface2,(270,290))
    quit_box=pg.draw.rect(window,(255, 141, 141),(550,565,250,75))
    window.blit(pg.font.Font(None, 36).render("QUIT", True, (255,0,61)), (647,593))
    play_again=pg.draw.rect(window,(137, 255, 159),(125,565,250,75))
    window.blit(pg.font.Font(None, 36).render("RESET BOARD", True, (6, 85, 53)), (161,593))
    pg.display.flip()
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
    i,f=0.005,1/1.2
    def roller(self):
        self.is_rolling=True
        self.i,self.f=0.005,1/1.2
    
    def rolling(self,src):
        self.i,self.f=0.005,1/1.2
        while True:
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
                break
            self.i*=self.f
        src.load()
        p1.img_load()
        p2.img_load()
        del self.i,self.f
        return self.roll(src)
 
    def roll(self,src):
        self.roll_no=randint(0,5)
        for self.i in range (3):
            self.x=725
            self.y=355
            window.blit(self.dice_tuple[self.roll_no],(self.x,self.y))
            roll_text=pg_img_loader.font_36.render("  DICE", True, (237, 224, 200))
            window.blit(roll_text,(730,325))
            pg.display.flip()
            sleep(1)
            src.load()
            p1.img_load()
            p2.img_load()
            roll_text=pg_img_loader.font_36.render("  DICE", True, (237, 224, 200))
            window.blit(roll_text,(730,325))
            pg.display.flip()
            sleep(1)
        del self.i
        return self.roll_no+1
class interchange_2_player:
    turn=1
    def swapper(self,p1,p2):
        global turn_player
        if self.turn:
            p1.move_multiple(dicee.rolling(pg_img_loader),p2,pg_img_loader)
            self.turn-=1
            turn_player=p2.name
        else:
            p2.move_multiple(dicee.rolling(pg_img_loader),p1,pg_img_loader)
            self.turn+=1
            turn_player=p1.name
        color_check()


class interchange_computer:
    turn=1
    def swapper(self,p1,p2):
        global turn_player
        p1.move_multiple(dicee.rolling(pg_img_loader),p2,pg_img_loader)
        turn_player=p2.name
        color_check()
        if(p1.square_no>=100):
            return
        sleep(2)
        p2.move_multiple(dicee.rolling(pg_img_loader),p1,pg_img_loader)
        turn_player=p1.name
        color_check()
        if(p2.square_no>=100):
            return


def color_check ():
    global player_turn_color
    if p1.square_no>p2.square_no:
        pg_img_loader.color=[36,81,161]
        player_turn_color=[102, 153, 204]
    elif p1.square_no<p2.square_no:
        pg_img_loader.color=[161, 36, 62]
        player_turn_color= [255, 229, 204]
    elif p1.square_no==p2.square_no:
        pg_img_loader.color=[51,51,51]
        player_turn_color=[192, 192, 192]
    if p1.square_no>=100 or p2.square_no>=100:
        pg_img_loader.color=[36, 113, 72]
    pg_img_loader.load()
    p1.img_load()
    p2.img_load()
    pg.display.flip()
if choice:
    player_change=interchange_2_player()
else:
    player_change=interchange_computer()
p1=player()
p1.path="resources/player_1.png"
p2=player()
p2.path="resources/player_2.png"
dicee=dice()
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
running_load=running_name=True
font_70 = pg.font.Font(None, 70)
font_36 = pg.font.Font("resources/test.ttf", 36)
r=g=b=255
title="SNL"
temp=temp1=1





if not is_started:
    user_name_1=""
    user_name_2=""
    while running_name:
        if not running_name:
            break
        for event in pg.event.get():  
            if event.type==pg.QUIT:
                running=running_name=False
                choice=0
            if event.type==pg.KEYDOWN:
                if event.key==pg.K_RETURN:
                    running_name=False
                    break
                if event.key==pg.K_BACKSPACE:
                    if user_name_1!=[]:
                        user_name_1=user_name_1[:-1]
                    continue
                user_name_1+=event.unicode
        window.fill((0,0,0))
        window.blit(font_36.render("ENTER PLAYER 1 NAME", True, (255,255,255)),(285,120))
        window.blit(font_36.render(user_name_1, True, (255,255,255)),(450,320))
        pg.display.flip()
        clockk.tick(fps)
    p1.name=user_name_1
    if choice:
        running_name_2=True
        while running_name_2:
            if not running_name_2:
                break
            for event in pg.event.get():  
                if event.type==pg.QUIT:
                    running=running_name_2=False
                if event.type==pg.KEYDOWN:
                    if event.key==pg.K_RETURN:
                        running_name_2=False
                        break
                    if event.key==pg.K_BACKSPACE:
                        if user_name_2!=[]:
                            user_name_2=user_name_2[:-1]
                        continue
                    user_name_2+=event.unicode
            window.fill((0,0,0))
            window.blit(font_36.render("ENTER PLAYER 2 NAME", True, (255,255,255)),(285,120))
            window.blit(font_36.render(user_name_2, True, (255,255,255)),(450,320))
            pg.display.flip()
            clockk.tick(fps)
        p2.name=user_name_2



    while running:
        if not running_load:break
        for event in pg.event.get():
            if event.type==pg.QUIT:
                running=False
            if event.type==pg.KEYDOWN and event.key==pg.K_RETURN:
                running_load=False
                break
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

turn_player=p1.name
quit_box=pg.draw.rect(window,(255, 141, 141),(550,565,550,375))
play_again=pg.draw.rect(window,(137, 255, 159),(125,565,250,75))

while running:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running=False
        if event.type==pg.MOUSEBUTTONDOWN:
            if event.button==1:
                mouse_pos=pg.mouse.get_pos()
                if quit_box.collidepoint(mouse_pos):
                    if conf():
                        pg.display.flip()
                        running=False
                    else:
                        pg_img_loader.load()
                if play_again.collidepoint(mouse_pos):
                    if conf():
                        p1.square_no=p2.square_no=1
                        p1.pos_x=188
                        p1.pos_y=428
                        p2.pos_x=188
                        p2.pos_y=428
                        turn_player=p1.name
                        color_check()
                        player_change.turn=1
                        p1.img_load()
                        p2.img_load()
                        pg_img_loader.load()
                        pg.display.flip()
                    else:
                        pg_img_loader.load()
        if p1.square_no>=100 or p2.square_no>=100:break
        if (event.type==pg.KEYDOWN and event.key==pg.K_SPACE) or (event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and pg_img_loader.button_rect.collidepoint(event.pos) and not is_clicked):
                is_clicked = True
                if is_both_players_on_same_square:
                    p2.pos_y-=2
                    p1.pos_y+=2
                    is_both_players_on_same_square=0
                dicee.roller()
                player_change.swapper(p1,p2)
                if p1.square_no==p2.square_no:
                    is_both_players_on_same_square=1
                    p1.pos_y-=2
                    p2.pos_y+=2
        if event.type == pg.MOUSEBUTTONUP and event.button == 1:
            is_clicked = False
    if(p1.square_no>=100):
        win()
        sleep(1)
        continue
    if(p2.square_no>=100):
        win()
        sleep(1)
        continue
    pg_img_loader.load()
    pg_img_loader.roll_button()
    p1.img_load()
    p2.img_load()
    quit_box=pg.draw.rect(window,(255, 141, 141),(550,565,250,75))
    window.blit(pg.font.Font(None, 36).render("QUIT", True, (255,0,61)), (647,593))
    play_again=pg.draw.rect(window,(137, 255, 159),(125,565,250,75))
    window.blit(pg.font.Font(None, 36).render("RESET BOARD", True, (6, 85, 53)), (161,593))
    pg.display.flip()

pg.quit()
print("\t\tThanks for playing\n\n\t\tA Program by TBA5854")     