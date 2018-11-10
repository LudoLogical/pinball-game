import pygame
from objects.circle import Circle

class Ball(Circle):
    def __init__(self,x,y,r,color,spd,name="ball"):
        super().__init__(x,y,r,color,spd,name)
        self.vx = 0
        self.vy = 0

    def accelerate(self):
        self.vy += TABLE_ACCELERATION

    def draw(self, ctx):
        pygame.draw.circle(ctx,self.color,(self.x,self.y),self.r)
