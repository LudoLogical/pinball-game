import pygame, constants
from logic import collisions
from img import images
from sound import sounds
from objects.rect import Rect

class Item(Rect):
    def __init__(self,id,w,xShift=0,yShift=0,name="item"):
        super().__init__((constants.gameW-w)/2+xShift,(constants.gameH-w)/2+yShift,w,w,None,None,[0,0],name)
        self.id = id
        self.consumedFlag = False

    def activate(self, target):
        if self.id == 0: # peach
            sounds.play("chomp")
            if target.hp + 2 > target.maxHP:
                target.hp = target.maxHP
            else:
                target.hp += 2
        elif self.id == 1: # foodstamp
            sounds.play("paper")
            target.stamps += 1
        elif self.id == 2: # basil
            pass
        elif self.id == 3: # paprika
            if target.atkSpd > 5:
                target.atkSpd -= 2
            else:
                target.spd[0] += 1
                target.spd[1] += 1
        elif self.id == 4: # pepper
            target.spd[0] += 1
            target.spd[1] += 1
        elif self.id == 5: # salt
            pass
        elif self.id == 6: # tumeric
            pass
        elif self.id == 7: # giant-peach
            sounds.play("chomp")
            target.maxHP += 2
            target.hp = target.maxHP
        elif self.id == 8: # knife
            target.dmg += 1
        elif self.id == 9: #
            pass
        self.consumedFlag = True

        if self.id not in [0,1,7]:
            target.items.append(self)

    def setup(self):
        self.img = images.items[self.id]

    def go(self, ctx, player, roomCleared):
        if roomCleared:
            super().go(ctx)
            if collisions.rectangles(self, player):
                self.activate(player)
