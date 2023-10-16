# A grid of shapes using translate() and savedState() 
# that randomly draws a rectangle or oval

# set a background colour
#fill(0)
#rect(0, 0, width(), height())

# set the grid size
columns = 50
rows = 50

shapeWidth = width()/columns
shapeHeight = height()/rows

# loop through rows
for currentRow in range(rows):
    
    # saving the position at the start of the row will help
    # when you want to come back after looping through the columns
    with savedState():
        
        # loop through columns
        for currentCol in range(columns):
        
            # pick a colour
            fill(random(), random(), random())
            
            # pick a random number to determine
            # which shape you will draw
            if random() < 0.5:
                rect(0, 0, shapeWidth, shapeHeight)
            else:
                oval(0, 0, shapeWidth, shapeHeight)
            
            # move along to the next column
            translate(shapeWidth, 0)
            
    # move along to the next row
    translate(0, shapeHeight)
    
saveImage('_exports/random-shapes.jpg')