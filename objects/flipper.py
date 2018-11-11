import pygame, math
import constants
from logic import collisions
from objects.rect import Rect

class Flipper(Rect):
    def __init__(self,x,y,w,h,angle,activeAngle,color,spd=[0,0],name="flipper"):
        super().__init__(x,y,w,h,color,spd,name)
        self.angle = angle
        self.activeAngle = activeAngle

        self.angleCoords = self.prepCoords(angle)
        self.activeAngleCoords = self.prepCoords(activeAngle)

    def prepCoords(self, theta):
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

            xnew = coOrds[n][0] * math.cos(theta) - coOrds[n][1] * math.sin(theta)
            ynew = coOrds[n][0] * math.sin(theta) + coOrds[n][1] * math.cos(theta)

            coOrds[n] = [xnew + rotateX, ynew + rotateY]

        return coOrds

    def draw(self, ctx, isActive):

        if isActive:
            pygame.draw.polygon(ctx, self.color, self.activeAngleCoords, 0)
        else:
            pygame.draw.polygon(ctx, self.color, self.angleCoords, 0)

    def go(self, ctx, isActive):
        self.pos()
        self.draw(ctx, isActive)
