import pygame, constants, copy, math, mouse
from logic import collisions
from logic.graphics import sortByX, sortByY
from pygame import gfxdraw
from img import images
from objects.circle import Circle
from objects.rect import Rect

class Ball(Circle):

    bounciness = 0.8

    def __init__(self,x,y,r,color,img=None,name="ball"):
        super().__init__(x,y,r,color,[0,0],name)
        self.img = img
        self.score = 0
        self.launching = True

    def reset(self):
        self.x = constants.gameW - 20
        self.y = constants.gameH - 60
        self.spd = [0,0]
        self.launching = True

    def accelerate(self):
        pass
        self.spd[1] += constants.TABLE_ACCELERATION

    def checkFlipperHit(self, flipper):
        flipCoords = copy.deepcopy(flipper.angleCoords)
        flipCoords.sort(key=sortByY)

        small, big = 0, 0

        if flipper.angle < flipper.activeAngle:
            small = flipper.angle
            big = flipper.activeAngle
        else:
            small = flipper.activeAngle
            big = flipper.angle

        vertLeeway = abs(flipper.h*math.cos(5*math.pi/36))
        if collisions.circPie(self, Circle(flipper.pivotX,flipper.y,flipper.w,None), small, big) \
            or collisions.circleTiltedRect(self, flipper.currentCoords(), flipper.w, flipper.h, flipper.getAngle()):
            while collisions.circleTiltedRect(self, flipCoords, flipper.w, flipper.h, flipper.getAngle()):
                self.y -= 2

            self.bounce(flipper.getAngle())

            if flipper.name == "L":
                naturalModifier = 5*math.pi/36
            elif flipper.name == "R":
                naturalModifier = -5*math.pi/36
            else:
                print("Done goofed @ ball flipper hit")

            self.spd[0] -= -flipper.power*math.cos(naturalModifier + math.pi/2)
            self.spd[1] -= flipper.power*math.sin(naturalModifier + math.pi/2)
            self.x += self.spd[0]
            self.y += self.spd[1]


    def moveIllegal(self, ctx, flippers, bases, walls, bumpers, bricks):
        for f in flippers:
            if collisions.circleTiltedRect(self, f.currentCoords(), f.w, f.h, f.getAngle()):
                return f.getAngle()
        for b in bases:
            flipCoords = copy.deepcopy(b.points)
            flipCoords.sort(key=sortByY)
            w = abs((flipCoords[2][0]-flipCoords[0][0]))
            h = abs((flipCoords[1][1]-flipCoords[0][1]))
            if collisions.circleTiltedRect(self, flipCoords, w, h, b.angle):
                return b.getAngle()
        for w in walls:
            collides = collisions.circleRect(self, w)
            if collides:
                self.x -= self.spd[0]
                self.y -= self.spd[1]
                if collides == 1 or collides == 3:
                    self.spd[0] *= -self.bounciness
                if collides == 2 or collides == 3:
                    self.spd[1] *= -self.bounciness
                self.x += self.spd[0]
                self.y += self.spd[1]
        for bb in bumpers:
            if collisions.circles(self, bb):
                # Add those sweet, sweet points
                self.score += bb.points
                # We want to speed up from bumpers
                self.spd[0] *= 1.3
                self.spd[1] *= 1.3
                # The normal line is the line connecting centers
                # Therefore, the desired tangent angle output subtracts pi/2
                return math.atan2(self.y-bb.y, self.x-bb.x) - math.pi/2
        for bbb in bricks:
            if collisions.circleRect(self,Rect(bbb.xRange[0], bbb.y, bbb.xRange[1]-bbb.xRange[0], bbb.h, None)):
                self.score += bbb.points

        return None

    def bounce(self, surfaceAngle):

        # [newvx, newvy]=[oldvx, oldvy]−[C*normalx, C*normaly] where C = 2oldvxnx + 2oldvyny

        normalAngle = surfaceAngle + math.pi/2
        normalX = math.cos(normalAngle)
        normalY = math.sin(normalAngle)

        constant = 2*(self.spd[0]*normalX + self.spd[1]*normalY)

        self.spd[0] -= constant*normalX * self.bounciness
        self.spd[1] -= constant*normalY * self.bounciness

    def pos(self, ctx, flippers, bases, walls, bumpers, bricks):
        if self.launching:
            self.x += self.spd[0]
            self.y += self.spd[1]
            if self.y <= 47:
                self.spd[0] = -8
                self.spd[1] = -1
            if self.x <= constants.gameW - (40+self.r):
                self.launching = False
        else:
            self.accelerate()
            self.x += self.spd[0]
            self.y += self.spd[1]
            bounceAngle = self.moveIllegal(ctx, flippers, bases, walls, bumpers, bricks)
            if bounceAngle != None:
                self.x -= self.spd[0]
                self.y -= self.spd[1]
                self.bounce(bounceAngle)
                self.x += self.spd[0]
                self.y += self.spd[1]
        #self.x = mouse.mouse['pos'][0]
        #self.y = mouse.mouse['pos'][1]

    def draw(self, ctx):
        if self.img != None:
            ctx.blit(self.img,(int(self.x) - self.r, int(self.y) - self.r))
        else:
            gfxdraw.filled_circle(ctx,int(self.x),int(self.y),self.r,self.color)
            gfxdraw.aacircle(ctx,int(self.x),int(self.y),self.r,self.color)

    def go(self, ctx, flippers, bases, walls, bumpers, bricks):
        self.pos(ctx, flippers, bases, walls, bumpers, bricks)
        self.draw(ctx)
