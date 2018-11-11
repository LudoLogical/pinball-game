import pygame, constants

# ball = pygame.transform.scale(pygame.image.load("img/ball.png"),(40,40))
menu = pygame.transform.scale(pygame.image.load("img/menu.png"),(constants.gameW,constants.gameH))

flippers = {
    'inactive': {
        'L': pygame.transform.scale(pygame.image.load("img/lflip.png"),(120,80)),
        'R': pygame.transform.scale(pygame.image.load("img/rflip.png"),(120,80))
    },
    'active': {
        'L': pygame.transform.scale(pygame.image.load("img/lflipactive.png"),(120,80)),
        'R': pygame.transform.scale(pygame.image.load("img/rflipactive.png"),(120,80))
    },
}
