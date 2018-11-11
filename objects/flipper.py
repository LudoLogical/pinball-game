import pygame, math
import constants
from logic import collisions
from objects.rect import Rect

class Flipper(Rect):
    def __init__(self,x,y,w,h,angle,color,spd=[0,0],name="flipper"):
        super().__init__(x,y,w,h,color,spd,name)
        self.angle = angle

    def draw(self, ctx):

        coOrds = [[self.x - self.w/2, self.y - self.h/2],
                [self.x + self.w/2, self.y - self.h/2],
                [self.x + self.w/2, self.y + self.h/2],
                [self.x - self.w/2, self.y + self.h/2]]

        if self.w > self.h:
            rotateX = self.x - (self.w/2 - self.h/2)
            rotateY = self.y
        else:
            rotateX = self.x
            rotateY = self.y - (self.h/2 - self.w/2)

        for n in range(0,len(coOrds)):

            coOrds[n][0] -= rotateX
            coOrds[n][1] -= rotateY

            xnew = coOrds[n][0] * math.cos(self.angle) - coOrds[n][1] * math.sin(self.angle)
            ynew = coOrds[n][0] * math.sin(self.angle) + coOrds[n][1] * math.cos(self.angle)

            coOrds[n] = [xnew + rotateX, ynew + rotateY]

        pygame.draw.polygon(ctx, self.color, coOrds, 0)
