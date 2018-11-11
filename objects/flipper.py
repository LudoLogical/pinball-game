import pygame, math, constants, copy
from pygame import gfxdraw
from img.images import flippers
from logic import collisions
from logic.graphics import sortByX, sortByY
from objects.rect import Rect

class Flipper(Rect):
    def __init__(self,x,y,w,h,angle,activeAngle,color,name="flipper"):
        super().__init__(x,y,w,h,color,None,[0,0],name)
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

    def getHighestPoints(self):
        temp = copy.deepcopy(self.angleCoords)
        temp.sort(key=sortByY)
        return temp[0], temp[1]

    def draw(self, ctx, isActive):

        if isActive:
            gfxdraw.filled_polygon(ctx, self.activeAngleCoords, self.color)
            gfxdraw.aapolygon(ctx, self.activeAngleCoords, self.color)
        else:
            gfxdraw.filled_polygon(ctx, self.angleCoords, self.color)
            gfxdraw.aapolygon(ctx, self.angleCoords, self.color)

    def go(self, ctx, isActive):
        self.pos()
        self.draw(ctx, isActive)
