def bucketFill(testArray, startX, startY, searchChar='y', fillChar='f'):
    if testArray[startY][startX]==searchChar:
        testArray[startY][startX]=fillChar
        # print("Set [", startX, "][", startY, "] to ",testArray[startY][startX])
        if startY > 0:
            bucketFill(testArray,startX,startY-1)
        if startY < len(testArray)-1:
            bucketFill(testArray,startX,startY+1)
        if startX > 0:
            bucketFill(testArray,startX-1,startY)
        if startX < len(testArray[0])-1:
            bucketFill(testArray,startX+1,startY)
