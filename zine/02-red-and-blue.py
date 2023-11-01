# define our constants
inch = 72
cropWidth = 5.83 * inch 
cropHeight = 8.27 * inch
bleed = 0.125 * inch

# do i want to see the bleed?
# NOTE! make this false before exporting
drawBleed = True

# calculate the total width and height
totalWidth = cropWidth+bleed*2
totalHeight = cropHeight+bleed*2

# make a new page
newPage(totalWidth, totalHeight)

with savedState():
    if drawBleed:    
        # draw the crop areas
        stroke(1, 0, 0)
        fill(None)
        strokeWidth(.5)
        rect(bleed, bleed, cropWidth, cropHeight)
    
    
    
######    

    cubeW = totalWidth / 15
    cubeH = totalHeight / 19
    red = 212/255, 6/255, 6/255
    blue = 26/255, 37/255, 83/255

    offset = True

    for row in range(19):
        if row % 2 :
            offset = True
        else :
            offset = False
    
        with savedState():
            for column in range (15):
                # set colour for the background squares
                if offset : 
                    fill(*red)
                else :
                    fill(*blue)
    
                # draw the square
                rect(0, 0, cubeW, cubeH)
        
                # set colour for the foreground shapes
                if offset :
                    fill(*blue)
                else :
                    fill(*red)
    
                # draw the shape
                # the shape depends on the row/column combo
                if (column in range(4, 10)) and (row in range(4, 15)) :
                    if column != 9 :
                        rect(cubeW/4, cubeH/4, cubeW/2, cubeH/2)
                    else :
                        oval(cubeW/6, cubeH/6, cubeW/1.5, cubeH/1.5)
                else :
                    oval(cubeW/6, cubeH/6, cubeW/1.5, cubeH/1.5)
            
                translate(cubeW, 0)
                offset = not offset
        translate(0, cubeH)
    
    
######    
        
# move to the (0, 0) of the cropped page, if you want
translate(bleed, bleed)

saveImage('_exports/02-red-and-blue.jpg')