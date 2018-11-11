import pygame, constants
from pygame import gfxdraw
from img import images
from objects.circle import Circle

class Ball(Circle):
    def __init__(self,x,y,r,color,img=None,name="ball"):
        super().__init__(x,y,r,color,[0,0],name)
        self.img = img

    def accelerate(self):
        pass
        #self.spd[1] += constants.TABLE_ACCELERATION

    def pos(self):
        self.accelerate()
        self.y += self.spd[1]

    def draw(self, ctx):
        if self.img != None:
            ctx.blit(self.img,(int(self.x) - self.r, int(self.y) - self.r))
        else:
            gfxdraw.filled_circle(ctx,int(self.x),int(self.y),self.r,self.color)
            gfxdraw.aacircle(ctx,int(self.x),int(self.y),self.r,self.color)
