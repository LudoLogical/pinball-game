import pygame
from objects.rect import Rect

class Obstruction(Rect):
    def __init__(self,x,y,w,h,spd=[0,0],name="obstruction"):
        super().__init__(x,y,w,h,None,spd,name)
