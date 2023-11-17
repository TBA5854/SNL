class animations:
    i=0
    t=3
    blinking_i=0
    blinking_t=1
    blinking_q=0
    def blinking(self,font_engine,text,r,g,b,coords):
        if self.blinking_i>40:self.blinking_i,self.blinking_t=40,-1
        if self.blinking_i<0:self.blinking_i,self.blinking_t=0,1
        self.blinking_i+=self.blinking_t
        if self.blinking_t>0:window.blit(font_engine.render(text,True,[r,g,b]),coords)
    def breathing(self,font_engine,text,r,g,b,coords):
        if max(r,g,b)>=255:self.t=-1*3
        if min(r,g,b)<=0:self.t=+1*3
        self.i+=self.t
        window.blit(font_engine.render(text,True,[r+self.i,g+self.i,b+self.i]),coords)


animator=animations()