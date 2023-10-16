# Draw a brick wall

brickWidth = 215
brickHeight = 65

columns = round(width()/brickWidth)
rows = round(height()/brickHeight)

# set mortar colour
fill(0.8, 0.8, 0.7)
rect(0, 0, width(), height())

overflow = brickWidth

# loop through rows
for currentRow in range(rows):
    
    # keep track of length of bricks placed on a row
    bricksRow = 0
    
    # saving the position at the start of the row will help
    # when you want to come back after looping through the columns
    with savedState():
        
        
        # loop through columns
        for currentCol in range(columns):
            
            # the first brick follows from the last one on the previous row
            if currentCol == 0:
                currentBrick = overflow
            else :
                currentBrick = brickWidth

            # vary the brick colour
            if random() < 0.5 :
                fill(0.5, 0, 0)
            else :
                fill(0.4, 0, 0)

            rect(0, 0, currentBrick, brickHeight)
            
            # move along to the next column
            # add mortar allowance
            translate(currentBrick+5, 0)
            
            bricksRow = bricksRow + currentBrick + 5
            
        # check the overflowing state of the brick row
        # the abs() bit turns it into a positive number
        # you need the overflow to be positive in case it will 
        # become the next brick width
        overflow = abs(bricksRow - width())
        
        # if there is space left over put another brick down
        if bricksRow < width() :
            rect(0, 0, overflow, brickHeight)
                    
    # move along to the next row
    # add mortar allowance
    translate(0, brickHeight+5)

saveImage('_exports/brick-wall.jpg')
