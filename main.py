import pygame, constants, math
import keyboard, mouse
from pygame import gfxdraw
from logic import collisions
from img import images
from objects.polygon import Polygon
from objects.rect import Rect
from objects.flipper import Flipper
from objects.ball import Ball
from objects.bumper import Bumper

# Window will spawn in exact center
import os
from win32api import GetSystemMetrics
windowX = GetSystemMetrics(0)/2 - constants.gameW/2
windowY = GetSystemMetrics(1)/2 - constants.gameH/2
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (windowX, windowY)

pygame.init()
from pygame.locals import NOFRAME, DOUBLEBUF #FULLSCREEN
ctx = pygame.display.set_mode((constants.gameW,constants.gameH), DOUBLEBUF)

ctx.set_alpha(None)
pygame.display.set_caption("Pinball")
clock = pygame.time.Clock()

def listen(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
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
    state = constants.TITLE_SCREEN

    playButton = Rect(constants.gameW/2-105, constants.gameH-200, 210, 63, None, images.playButton)

    ball = Ball(300,50,10,constants.colors['ball'])

    # PREP FOR FLIPPERS
    leftX = -15 + constants.gameW/2-45
    rightX = 15 + constants.gameW/2+45 + 2*35
    flippers = [
        Flipper(leftX,550,90,20,5*math.pi/36,-5*math.pi/36,constants.colors['flipper'],"L"),
        Flipper(rightX,550,90,20,31*math.pi/36,41*math.pi/36,constants.colors['flipper'],"R")
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
        Polygon([leftmostTop,leftHigh,left2ndHigh,leftmostBot],flippers[0].angle,constants.colors['wall']),
        Polygon([rightmostTop,rightHigh,right2ndHigh,rightmostBot],flippers[1].angle,constants.colors['wall'])
    ]

    walls = [
        Rect(0,0,constants.gameW,10,constants.colors['wall']),
        Rect(0,0,20,constants.gameH,constants.colors['wall']),
        Rect(constants.gameW-40,0,40,constants.gameH,constants.colors['wall'])
    ]
    bumpers = [Bumper(60,60),Bumper(175,145),Bumper(265,130),Bumper(240,210),
                Bumper(100,270,50,None,images.burst,"superbumper")]

    while running:
        running = listen(running)

        if state == constants.TITLE_SCREEN:
            ctx.blit(images.menu,(0,0))
            playButton.go(ctx)
            if mouse.mouse['click'] and collisions.rectPoint(playButton,mouse.mouse['pos']):
                state = constants.STAGE_ONE

        elif state == constants.STAGE_ONE:

            ctx.fill(constants.colors['bg'])

            for b in bases:
                b.go(ctx)
            for w in walls:
                w.go(ctx)
            for f in flippers:
                f.go(ctx, ball)
            for bb in bumpers:
                bb.go(ctx)

            gfxdraw.filled_polygon(ctx,[[350,0],[400,0],[400,50]],constants.colors['releaser'])
            gfxdraw.aapolygon(ctx,[[350,0],[400,0],[400,50]],constants.colors['releaser'])

            ctx.blit(images.brick,(20,130))
            ctx.blit(images.button,(320,320))


            ball.go(ctx, flippers, bases, walls, bumpers)

            # Debug
            # pygame.draw.rect(ctx,constants.colors['white'],(leftX-35,550,1,1))
            # pygame.draw.rect(ctx,constants.colors['white'],(rightX-35,550,1,1))
            pygame.draw.rect(ctx,constants.colors['white'],(flippers[0].pivotX,flippers[0].y,1,1))
            # midline.go(ctx)
            fpsTEXT = str(round(clock.get_fps(),1))
            fps = constants.muli["15"].render(fpsTEXT,True,constants.colors['black'])
            ctx.blit(fps,(25,8))

        # Update Window
        pygame.display.update()
        # input()
        clock.tick(60)

    pygame.quit()

main()
