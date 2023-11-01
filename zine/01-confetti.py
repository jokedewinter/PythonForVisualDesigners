# define our constants
inch = 72
cropWidth = 5.83 * inch 
cropHeight = 8.27 * inch
bleed = 0.125 * inch

# do i want to see the bleed?
# NOTE! make this false before exporting
drawBleed = False

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


    W = round(width())
    H = round(height())
    
    # Create a lot of blobs
    for step in range(1000):
        # Determine the size of the shape
        shapeWidth = randint(20, round(W/5))
        shapeHeight = randint(20, round(W/5))
    
        # Determine position of shape
        x = randint(-shapeWidth, round(W))
        y = randint(-shapeHeight, round(H))
        # Pick a colour
        opacity = (shapeWidth/W)*10
        fill(random(), random(), random(), .5)
        # Draw the shape
        oval(x, y, shapeWidth, shapeHeight)
        
# move to the (0, 0) of the cropped page, if you want
translate(bleed, bleed)

saveImage('_exports/01-confetti.pdf')