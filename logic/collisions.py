import math, copy
from logic.graphics import sortByX, sortByY
from objects.rect import Rect

def linePoint(x1, y1, x2, y2, px, py):
    # get distance from the point to the two ends of the line
    d1 = math.hypot(px-x1,py-y1)
    d2 = math.hypot(px-x2,py-y2)

    # get the length of the line
    lineLen = math.hypot(x2-x1,y2-y1)

    # add buffer zone that will give collision
    epsilon = 0.1; # higher val = less accurate

    # if the two distances are equal to the line's
    # length, the point is on the line!
    # note we use the buffer here to give a range,
    # rather than one val
    if (d1+d2 >= lineLen-epsilon and d1+d2 <= lineLen+epsilon):
        return True
    else:
        return False

def rectPoint(rect,point):
    if rect.x < point[0]:
        if rect.x + rect.w > point[0]:
            if rect.y < point[1]:
                if rect.h + rect.y > point[1]:
                    return True
    return False

def rectangles(a,b): # exception is for player's rBall addition
    if a.x < b.x + b.w:
        if a.x + a.w > b.x:
            if a.y < b.y + b.h:
                if a.h + a.y > b.y:
                    dx = abs((a.x+a.w/2)-(b.x+b.w/2)) / b.w
                    dy = abs((a.y+a.h/2)-(b.y+b.h/2)) / b.h
                    if dy < dx: return 1
                    else: return 2
    return 0

def circPoint(circ,point):
    dx = point[0] - circ.x
    dy = point[1] - circ.y
    dd = math.hypot(dx, dy)

    if dd <= circ.r:
        return True
    else:
        return False

def circles(a,b):
    # if distance between their centers is less than the sum of their radii
    dx = abs(a.x - b.x)
    dy = abs(a.y - b.y)
    dt = math.hypot(dx,dy)
    if dt < a.r + b.r:
        return True
    return False

def circPie(circ, pie, pieLowTheta, pieHighTheta):

    if not circles(circ,pie):
        return False
    else:
        # Bounding line test covered by flippers themselves; duplicate code
        # if lineCircle(pie.x,pie.y,pie.r*math.cos(pieLowTheta),pie.r*math.sin(pieLowTheta),circ):
        #     return True
        # elif lineCircle(pie.x,pie.y,pie.r*math.cos(pieHighTheta),pie.r*math.sin(pieHighTheta),circ):
        #     return True
        # else:
            dx = circ.x - pie.x
            dy = circ.y - pie.y
            internalTheta = math.atan2(dy,dx)
            if (internalTheta > pieLowTheta and internalTheta < pieHighTheta) \
                or (internalTheta + math.tau > pieLowTheta and internalTheta + math.tau < pieHighTheta):
                return True
            else:
                return False

def circleRect(circ,rect):
    # get x and y distance from their centers
    dx = abs(circ.x - rect.x - rect.w / 2)
    dy = abs(circ.y - rect.y - rect.h / 2)
    dxMin = abs(rect.w / 2) + circ.r
    dyMin = abs(rect.h / 2) + circ.r

    # test collision, return false if not colliding
    if dx > dxMin: return False
    elif dy > dyMin: return False
    # elif dx <= rect.w / 2: return True
    # elif dy <= rect.h / 2: return True

    # find bounce direction, return associated number
    if dy / rect.h < dx / rect.w: # ratios dissociate from unequal sides of rectangles
        if dx + abs(circ.spd[0]) <= dxMin: # if this function would return true next tick
            return 3 # flip both directions
        else:
            return 1 # flip x direction
    else: # dx / rect.w < dy / rect.h:
        if dy + abs(circ.spd[1]) <= dyMin:
            return 3 # flip both directions
        else:
            return 2 # flip y direction

def circleTiltedRect(circ, rectPoints, rectW, rectH, rectAngle):

    rectAngle = math.tau - rectAngle

    temp = copy.deepcopy(rectPoints)
    temp.sort(key=sortByX)
    cX = (temp[3][0] + temp[0][0])/2
    temp.sort(key=sortByY)
    cY = (temp[3][1] + temp[0][1])/2

    rect = Rect(cX-rectW/2, cY-rectH/2, rectW, rectH, None)

    # Rotate circle's center point back
    unrotatedCircleX = math.cos(rectAngle) * (circ.x - cX) - math.sin(rectAngle) * (circ.y - cY) + cX
    unrotatedCircleY = math.sin(rectAngle) * (circ.x - cX) + math.cos(rectAngle) * (circ.y - cY) + cY

    closestX = 0
    closestY = 0

    # Find the unrotated closest x point from center of unrotated circle
    if unrotatedCircleX < rect.x:
        closestX = rect.x
    elif unrotatedCircleX > rect.x + rect.w:
        closestX = rect.x + rect.w
    else:
        closestX = unrotatedCircleX

    # Find the unrotated closest y point from center of unrotated circle
    if unrotatedCircleY < rect.y:
        closestY = rect.y
    elif unrotatedCircleY > rect.y + rect.h:
        closestY = rect.y + rect.h
    else:
        closestY = unrotatedCircleY

    # Determine collision
    dx = unrotatedCircleX - closestX
    dy = unrotatedCircleY - closestY

    if math.hypot(dx, dy) < circ.r:
        return True
    else:
        return False

def lineCircle(x1, y1, x2, y2, circ):
    # is either end INSIDE the circle?
    # if so, return true immediately
    inside1 = circPoint(circ, [x1,y1])
    inside2 = circPoint(circ, [x2,y2])
    if inside1 or inside2:
        return True

    # get length of the line
    lx = x1 - x2
    ly = y1 - y2
    length = math.hypot(lx,ly)

    # get dot product of the line and circle
    dot = ( ((circ.x-x1)*(x2-x1)) + ((circ.y-y1)*(y2-y1)) ) / math.pow(length,2)

    # find the closest point on the line
    closestX = x1 + (dot * (x2-x1))
    closestY = y1 + (dot * (y2-y1))

    # is this point actually on the line segment?
    # if so keep going, but if not, return false
    if not linePoint(x1,y1,x2,y2, closestX,closestY):
        return False

    # get distance to closest point
    dx = closestX - circ.x
    dy = closestY - circ.y
    dd = math.hypot(dx, dy)

    if dd <= circ.r:
        return True
    else:
        return False
