import pygame, constants
from pygame import gfxdraw
from img import images
from logic import collisions
from objects.rect import Rect

class Brick(Rect):
    def __init__(self,x,y,w,h,min,max,points=20,img=images.brick,name="brick"):
        super().__init__(x,y,w,h,None,img,[0,0],name)
        self.xRange = [min,max]
        self.points = points
