import pygame, math
from logic import collisions
from sound import sounds
from objects.rect import Rect

class Bullet(Rect):
    def __init__(self,x,y,w,h,img,angle,dmg,name="bullet"):
        super().__init__(x,y,w,h,None,img,[8*math.cos(angle),8*math.sin(angle)],name)
        self.removeFlag = False
        self.dmg = dmg

    def pos(self, room):
        self.x += self.spd[0]
        self.y += self.spd[1]
        if not self.canMove(room):
            sounds.play("loud_thump")
            self.removeFlag = True

    def go(self, ctx, room, player):
        self.pos(room)
        self.draw(ctx)
        if self.name == "good":
            for e in room["enemies"]:
                if collisions.rectangles(self,e) and e.hp > 0:
                    sounds.play("squish")
                    self.removeFlag = True
                    e.hp -= self.dmg
        elif self.name == "bad":
            if collisions.rectangles(self,player):
                self.removeFlag = True
                player.hp -= self.dmg
