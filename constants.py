import pygame
pygame.font.init()

# GENERAL VARIABLES
gameW, gameH = 400, 600
playerW, playerH = 60, 120
gridLength = 5

# COLORS
black = (0,0,0)
grey = (128,128,128)
minigrey = (178,178,178)
yellow = (255,255,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
lightpurple = (86,95,120)

# FONTS
muli = {
    "15": pygame.font.Font("fonts/muli.ttf",15),
    "20": pygame.font.Font("fonts/muli.ttf",20),
    "30": pygame.font.Font("fonts/muli.ttf",30),
    "70": pygame.font.Font("fonts/muli.ttf",70)
}

# WASD
W, A, S, D = 0, 1, 2, 3

# ACCELERATION // 1.11m/s
TABLE_ACCELERATION = 1
