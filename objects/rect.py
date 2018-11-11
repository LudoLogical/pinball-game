import pygame, constants
from pygame import gfxdraw
from logic import collisions
from objects.entity import Entity

class Rect(Entity):
    def __init__(self,x,y,w,h,color,img=None,spd=[0,0],name="rect"):
        super().__init__(x,y,color,spd,name)
        self.w = w
        self.h = h
        self.img = img

    def canMove(self, room):
        for o in room["obstructions"]:
            if collisions.rectangles(self,o):
                return False
        if self.x < 0 or self.y < 0 or self.x + self.w > constants.gameW or self.y + self.h > constants.gameH:
            return False
        return True

    def draw(self, ctx):
        if self.img != None:
            ctx.blit(self.img,(self.x,self.y))
        else:
            gfxdraw.rectangle(ctx,(self.x,self.y,self.w,self.h),self.color)
