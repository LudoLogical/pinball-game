import pygame, constants, math
import keyboard, mouse
from logic import collisions
from img import images
from objects.polygon import Polygon
from objects.rect import Rect
from objects.flipper import Flipper
from objects.ball import Ball

# Window will spawn in exact center
import os
from win32api import GetSystemMetrics
windowX = GetSystemMetrics(0)/2 - constants.gameW/2
windowY = GetSystemMetrics(1)/2 - constants.gameH/2
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (windowX, windowY)

# If ya don't boop
# angle = -90 + 2*(n-90)
# speed = 0.8v

# If ya boop
# angle =
# speed = 1.6v

pygame.init()
from pygame.locals import NOFRAME, DOUBLEBUF #FULLSCREEN
ctx = pygame.display.set_mode((constants.gameW,constants.gameH), DOUBLEBUF)

ctx.set_alpha(None)
pygame.display.set_caption("Pinball")
clock = pygame.time.Clock()

def listen(running):
    for event in pygame.event.get():
        if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
            running = False
        # elif event.type == sounds.END_FLAG:
        #     sounds.changeMusic(sounds.overtureLoopTime)
        else:
            keyboard.listen(event)
            mouse.listen()
    return running

def main():

    # pygame.mixer.music.play()
    # midline = Rect(199,0,2,600,(0,0,0))

    running = True
    score = 0
    ball = Ball(50,50,10,(234,206,205))

    # PREP FOR FLIPPERS
    leftX = -15 + constants.gameW/2-45
    rightX = 15 + constants.gameW/2+45 + 2*35
    flippers = [
        Flipper(leftX,550,90,20,5*math.pi/36,-5*math.pi/36,(226, 135, 80),"L"),
        Flipper(rightX,550,90,20,31*math.pi/36,41*math.pi/36,(226, 135, 80),"R")
    ]

    # PREP FOR BASES
    leftHigh, left2ndHigh = flippers[0].getHighestPoints()
    leftXRate = math.tan(flippers[0].angle)
    leftmostTop = [0,leftHigh[1]-leftHigh[0]*leftXRate]
    leftmostBot = [0,left2ndHigh[1]-left2ndHigh[0]*leftXRate]
    rightHigh, right2ndHigh = flippers[1].getHighestPoints()
    rightXRate = -math.tan(flippers[1].angle)
    rightmostTop = [constants.gameW,rightHigh[1]-(constants.gameW-rightHigh[0])*rightXRate]
    rightmostBot = [constants.gameW,right2ndHigh[1]-(constants.gameW-right2ndHigh[0])*rightXRate]
    bases = [
        Polygon([leftmostTop,leftHigh,left2ndHigh,leftmostBot],flippers[0].angle,(30, 23, 36)),
        Polygon([rightmostTop,rightHigh,right2ndHigh,rightmostBot],flippers[1].angle,(30, 23, 36))
    ]

    walls = [
        Rect(0,0,constants.gameW,10,(30, 23, 36)),
        Rect(0,0,20,constants.gameH,(30, 23, 36)),
        Rect(constants.gameW-40,0,40,constants.gameH,(30, 23, 36))
    ]

    while running:
        running = listen(running)

        ctx.fill((56, 45, 62))

        for b in bases:
            b.go(ctx)
        for w in walls:
            w.go(ctx)
        for f in flippers:
            f.go(ctx, ball)

        ball.go(ctx, flippers, bases, walls)

        # Debug
        # pygame.draw.rect(ctx,(255,255,255,255),(leftX-35,550,1,1))
        # pygame.draw.rect(ctx,(255,255,255,255),(rightX-35,550,1,1))
        pygame.draw.rect(ctx,(255,255,255,255),(flippers[0].pivotX,flippers[0].y,1,1))
        # midline.go(ctx)
        fpsTEXT = str(round(clock.get_fps(),1))
        fps = constants.muli["15"].render(fpsTEXT,True,constants.black)
        ctx.blit(fps,(25,5))

        # Update Window
        pygame.display.update()
        # input()
        clock.tick(60)

    pygame.quit()

main()
