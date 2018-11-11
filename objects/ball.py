import pygame, constants, copy, math
from logic import collisions
from logic.graphics import sortByY
from pygame import gfxdraw
from img import images
from objects.circle import Circle

class Ball(Circle):
    def __init__(self,x,y,r,color,img=None,name="ball"):
        super().__init__(x,y,r,color,[0,0],name)
        self.img = img

    def accelerate(self):
        pass
        self.spd[1] += constants.TABLE_ACCELERATION

    def flipperHit(self, flippers):
        flipCoords = copy.deepcopy(flippers[0].angleCoords)
        flipCoords.sort(key=sortByY)
        print(flipCoords)
        if collisions.lineCircle(flipCoords[0][0],flipCoords[0][1],flipCoords[2][0],flipCoords[2][1],self):
            print("TOUCHING!!!!!!!")

    def moveIllegal(self, flippers, walls):
        for f in flippers:
            flipCoords = copy.deepcopy(f.angleCoords)
            flipCoords.sort(key=sortByY)
            if collisions.lineCircle(flipCoords[0][0],flipCoords[0][1],flipCoords[2][0],flipCoords[2][1],self):
                return f
        for w in walls:
            flipCoords = copy.deepcopy(w.points)
            flipCoords.sort(key=sortByY)
            if collisions.lineCircle(flipCoords[0][0],flipCoords[0][1],flipCoords[2][0],flipCoords[2][1],self):
                return w
        return None

    def bounce(self, surface):
        # angleOfAttack = math.atan2(self.spd[1],self.spd[0])
        normalAngle = surface.angle + math.pi/2
        normalX = math.cos(normalAngle)
        normalY = math.sin(normalAngle)

        constant = 2*(self.spd[0]*normalX + self.spd[1]*normalY)

        self.spd[0] -= constant*normalX
        self.spd[1] -= constant*normalY

    def pos(self, flippers, walls):
        self.accelerate()
        self.x += self.spd[0]
        self.y += self.spd[1]
        bounceSurface = self.moveIllegal(flippers, walls)
        if bounceSurface != None:
            self.x -= self.spd[0]
            self.y -= self.spd[1]
            self.bounce(bounceSurface)

    def draw(self, ctx):
        if self.img != None:
            ctx.blit(self.img,(int(self.x) - self.r, int(self.y) - self.r))
        else:
            gfxdraw.filled_circle(ctx,int(self.x),int(self.y),self.r,self.color)
            gfxdraw.aacircle(ctx,int(self.x),int(self.y),self.r,self.color)

    def go(self, ctx, flippers, walls):
        self.flipperHit(flippers)
        self.pos(flippers, walls)
        self.draw(ctx)
