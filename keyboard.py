import pygame
pygame.init()

presets = {
            'keyA':pygame.K_a,
            'keyS':pygame.K_s,
            'keyD':pygame.K_d,
            'keyF':pygame.K_f,
            'keyJ':pygame.K_j,
            'keyK':pygame.K_k,
            'keyL':pygame.K_l,
            'key;':pygame.K_SEMICOLON,
            'keySpace':pygame.K_SPACE,
            'keyEnter':pygame.K_RETURN,
            'keyEscape':pygame.K_ESCAPE
          }
controls = {
            'keyA':False,
            'keyS':False,
            'keyD':False,
            'keyF':False,
            'keyJ':False,
            'keyK':False,
            'keyL':False,
            'key;':False,
            'keySpace':False,
            'keyEnter':False,
            'keyEscape':False
           }

def listen(event):
        if event.type == pygame.QUIT:
            close()
        elif event.type == pygame.KEYDOWN:
            for p in presets:
                if event.key == presets[p]:
                    controls[p] = True
        elif event.type == pygame.KEYUP:
            for p in presets:
                if event.key == presets[p]:
                    controls[p] = False

def leftFlipper():
    if controls['keyA'] or controls['keyS'] or controls['keyD'] or controls['keyF']:
        return True
    else:
        return False

def rightFlipper():
    if controls['keyJ'] or controls['keyK'] or controls['keyL'] or controls['key;']:
        return True
    else:
        return False
