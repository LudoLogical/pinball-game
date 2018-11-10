import pygame, constants, math
from logic import collisions
from objects.rect import Rect
from objects.ball import Ball

# If ya don't boop
# angle = -90 + 2*(n-90)
# speed = 0.8v

# If ya boop
# angle =
# speed = 1.6v

# from pygame.locals import *
# flags = DOUBLEBUF

pygame.init()

# pygame.FULLSCREEN
ctx = pygame.display.set_mode((constants.gameW,constants.gameH))
# ctx = pygame.display.set_mode((constants.gameW,constants.gameH), flags)

ctx.set_alpha(None)
pygame.display.set_caption("Pinball")
clock = pygame.time.Clock()

def listen(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    return running

def main():

    # pygame.mixer.music.play()

    running = True
    score = 0

    while running:
        running = listen(running)
        # Reset BG
        ctx.fill((255,0,0))

        daBall = Ball(50,50,6,(255,255,0),5)
        daFlip = Rect(100,100,50,15,math.pi/6,(0,0,255))
        daFlip2 = Rect(100,100,50,15,-math.pi/6,(0,128,255))

        daBall.go(ctx)
        daFlip.go(ctx)
        daFlip2.go(ctx)

        score = score + 100

        # Debug
        fps = constants.muli["15"].render(str(round(clock.get_fps(),1)),True,constants.black)
        ctx.blit(fps,(840,575))

        # Update Window
        pygame.display.update()
        clock.tick(30)

    pygame.quit()

main()
# if game_over:
#myimage=PhotoImage(file='Gameover.gif')
#canvas.cr
