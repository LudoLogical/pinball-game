import pygame
from pygame import gfxdraw
from logic.graphics import sortByX, sortByY
from objects.entity import Entity

class Polygon(Entity):
    def __init__(self,points,angle,color,spd=[0,0],name="none"):
        super().__init__(0,0,color,spd,name)
        self.points = points
        self.angle = angle

    def draw(self, ctx):
        gfxdraw.filled_polygon(ctx, self.points, self.color)
        gfxdraw.aapolygon(ctx, self.points, self.color)
