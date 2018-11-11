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
ctx = pygame.display.set_mode((constants.gameW,constants.gameH), NOFRAME | DOUBLEBUF)

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

    running = True
    score = 0

    daBall = Ball(50,50,20,(234,206,205))

    leftX = -15 + constants.gameW/2-45
    rightX = 15 + constants.gameW/2+45 + 2*35

    daFlip = Flipper(leftX,550,90,20,5*math.pi/36,-5*math.pi/36,(226, 135, 80),"L")
    daFlip2 = Flipper(rightX,550,90,20,31*math.pi/36,41*math.pi/36,(226, 135, 80),"R")

    leftHigh, left2ndHigh = daFlip.getHighestPoints()
    leftXRate = math.tan(daFlip.angle)
    leftmostTop = [0,leftHigh[1]-leftHigh[0]*leftXRate]
    leftmostBot = [0,left2ndHigh[1]-left2ndHigh[0]*leftXRate]
    leftBase = Polygon([leftmostTop,leftHigh,left2ndHigh,leftmostBot],daFlip.angle,(0,0,0))

    rightHigh, right2ndHigh = daFlip2.getHighestPoints()
    rightXRate = -math.tan(daFlip2.angle)
    rightmostTop = [constants.gameW,rightHigh[1]-(constants.gameW-rightHigh[0])*rightXRate]
    rightmostBot = [constants.gameW,right2ndHigh[1]-(constants.gameW-right2ndHigh[0])*rightXRate]
    rightBase = Polygon([rightmostTop,rightHigh,right2ndHigh,rightmostBot],daFlip2.angle,(0,0,0))

    midline = Rect(199,0,2,600,(0,0,0))

    while running:
        running = listen(running)
        # Reset BG
        ctx.fill((56, 45, 62))

        leftBase.go(ctx)
        rightBase.go(ctx)

        midline.go(ctx)
        daBall.go(ctx, [daFlip, daFlip2], [leftBase, rightBase])
        daFlip.go(ctx, keyboard.leftFlipper())
        daFlip2.go(ctx, keyboard.rightFlipper())

        pygame.draw.rect(ctx,(255,255,255),(leftX,550,1,1))
        pygame.draw.rect(ctx,(255,255,255),(rightX,550,1,1))

        score = score + 100

        # Debug
        fpsTEXT = str(round(clock.get_fps(),1))
        fps = constants.muli["15"].render(fpsTEXT,True,constants.black)
        ctx.blit(fps,(15,15))

        # Update Window
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

main()
# if game_over:
#myimage=pygame.image.load(file='Gameover.gif')
# ctx.blit(myimage,(x,y))
#text_rect = text.get_rect()
    #    text_x = screen.get_width() / 2 - text_rect.width / 2
        #text_y = screen.get_height() / 2 - text_rect.height / 2
    #    screen.blit(text, [text_x, text_y])
