import pygame, math
import constants
from logic import collisions
from objects.entity import Entity

class Rect(Entity):
    def __init__(self,x,y,w,h,angle,color,img=None,spd=[0,0],name="rect"):
        super().__init__(x,y,color,spd,name)
        self.w = w
        self.h = h
        self.angle = angle
        self.img = img

    def canMove(self, room):
        for o in room["obstructions"]:
            if collisions.rectangles(self,o):
                return False
        if self.x < 0 or self.y < 0 or self.x + self.w > constants.gameW or self.y + self.h > constants.gameH:
            return False
        return True

    def draw(self, ctx):
        # if self.img != None:
        #     ctx.blit(self.img,(self.x,self.y))
        # else:
        #     pygame.draw.rect(ctx,self.color,(self.x,self.y,self.w,self.h))

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
