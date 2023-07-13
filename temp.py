import pygame as pg
from time import sleep
from random import randint
pg.init()
window=pg.display.set_mode((1000,720))
button_x=730
button_y=140
button_height=100
button_width=100
button_color=(180,140,140)
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
        font_36 = pg.font.Font(None, 36)
        font_70 = pg.font.Font(None, 70)
        
def win():
    win_rect=pg.draw.rect(window ,(255,255,255), (0, 120, 1000,600))
    if p1.square_no==100:
        win_text = "Player 1 Wins !!!"
    else:
        win_text = "Player 2 Wins !!!"
    
    text_surface2 = img_loader.font_70.render("ROLL", True, (randint(0,255), randint(0,255), randint(0,255)))
    window.blit(text_surface2,(450,240))
is_clicked=True
pg_img_loader=img_loader()
while running:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running=False
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect.collidepoint(event.pos) and not is_clicked:
                is_clicked = True
                print("Button clicked!")

        if event.type == pg.MOUSEBUTTONUP and event.button == 1:
            is_clicked = False

        pg_img_loader.load()
        button_rect=pg.draw.rect(window ,button_color, (button_x, button_y, button_width, button_height))
        win()
        pg.display.flip()
pg.quit()