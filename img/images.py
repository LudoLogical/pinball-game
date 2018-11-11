import pygame, constants

# ball = pygame.transform.scale(pygame.image.load("img/ball.png"),(40,40))
menu = pygame.transform.scale(pygame.image.load("img/menu.png"),(constants.gameW,constants.gameH))
playButton = pygame.transform.scale(pygame.image.load("img/playbutton.png"),(int(0.3*703),int(0.3*212)))

brick = pygame.transform.scale(pygame.image.load("img/redbrick.png"),(int(0.3*289),int(0.3*204)))
burst = pygame.transform.scale(pygame.image.load("img/blueburst.png"),(int(0.3*338),int(0.3*338)))
bumper = pygame.transform.scale(pygame.image.load("img/orangeface.png"),(int(0.3*128),int(0.3*128)))
button = pygame.transform.scale(pygame.image.load("img/button.png"),(int(0.3*254),int(0.3*300)))
plunger = pygame.transform.scale(pygame.image.load("img/startbouncything.png"),(20,60))
