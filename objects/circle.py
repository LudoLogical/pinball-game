import pygame
from objects.entity import Entity

class Circle(Entity):
    def __init__(self,x,y,r,color,spd,name="circle"):
        super().__init__(x,y,color,spd,name)
        self.r = r
    def draw(self, ctx):
        pygame.draw.circle(ctx,self.color,(self.x,self.y),self.r)
