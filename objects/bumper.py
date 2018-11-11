import pygame
from img import images
from objects.circle import Circle

class Bumper(Circle):
    def __init__(self,x,y,r=19,color=None,img=images.bumper,name="bumper"):
        super().__init__(x+r,y+r,r,color,[0,0],name)
        self.img = img
    def draw(self, ctx):
        if self.img != None:
            ctx.blit(self.img, (self.x-self.r,self.y-self.r))
        else:
            pygame.draw.circle(ctx,self.color,(self.x,self.y),self.r)
