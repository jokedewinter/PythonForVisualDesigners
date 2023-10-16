# Vasarely red and blue squares and circles

cube = 100
red = .8, .1, .1
blue = .2, .2, .4

newPage(1900, 1500)

offset = True

for row in range(15):
    if row % 2 :
        offset = True
    else :
        offset = False
        
    with savedState():
        for column in range (19):
            # draw the background squares
            if offset :
                fill(*red)
            else :
                fill(*blue)
        
            rect(0, 0, cube, cube)
            
            # draw the forground circles
            if offset :
                fill(*blue)
            else :
                fill(*red)
        
            oval(cube/6, cube/6, cube/1.5, cube/1.5)
            
            translate(cube, 0)
            offset = not offset
    translate(0, cube)
