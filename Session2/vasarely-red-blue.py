# Vasarely red and blue squares and circles

cube = 100
red = 212/255, 6/255, 6/255
blue = 26/255, 37/255, 83/255

newPage(1900, 1500)

offset = True

for row in range(15):
    if row % 2 :
        offset = True
    else :
        offset = False
        
    with savedState():
        for column in range (19):
            # set colour for the background squares
            if offset : 
                fill(*red)
            else :
                fill(*blue)
        
            # draw the square
            rect(0, 0, cube, cube)
            
            # set colour for the foreground shapes
            if offset :
                fill(*blue)
            else :
                fill(*red)
        
            # draw the shape
            # the shape depends on the row/column combo
            if (row in range(4, 10)) and (column in range(4, 15)) :
                if column != 9 :
                    rect(cube/4, cube/4, cube/2, cube/2)
                else :
                    oval(cube/6, cube/6, cube/1.5, cube/1.5)
            else :
                oval(cube/6, cube/6, cube/1.5, cube/1.5)
                
            translate(cube, 0)
            offset = not offset
    translate(0, cube)
    
saveImage('_exports/vasarely-red-blue.jpg')
