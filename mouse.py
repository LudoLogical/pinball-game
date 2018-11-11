import pygame
pygame.init()

mouse = {'pos':pygame.mouse.get_pos(),'click':0,'held':0}

def listen():
    mouse['pos'] = pygame.mouse.get_pos()
    info = pygame.mouse.get_pressed()
    if info[0] == 1 and mouse['held'] == 0:
        mouse['click'] = 1
        mouse['held'] = 1
    elif info[0] == 1 and mouse['held'] == 1:
        mouse['click'] = 0
    elif info[0] == 0:
        mouse['click'] = 0
        mouse['held'] = 0
