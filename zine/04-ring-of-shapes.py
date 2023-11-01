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

######

def triangle(size, direction):
    # Depending on the row value draw the rectangle pointing up
    # or pointing down.
    if direction % 2 :
        polygon(
            (-size/2,0), # bottom left 
            (size/2, 0), # bottom right
            (0, size) # top
        )
    else :
        polygon(
            # (0, size), # top left 
            # (size, size), # top right
            # (size/2, 0) # bottom
            (-size/2, size), # top left 
            (size/2, size), # top right
            (size/2, 0) # bottom
        )
    
def circleShapes(shapeCount=10, shapeSize=100, ringOffset=10, ring=1):
    with savedState():
        for shape in range(shapeCount):
            with savedState():
                translate(0, ringOffset)
                triangle(shapeSize, ring)
            rotate(360/shapeCount)
     

ringsTotal = 20
shapeSize = 5
shapeAmount = 31
offset = 10  
W = round(width())
H = round(height())
    
# Set background colour
fill(1)
rect(0, 0, W, H)
    
# Move to the center of the page
translate(W/2, H/2)

# Loop throught the amount of rings
for ring in range(ringsTotal) :
    
    fill(random(), random(), random())
    circleShapes(shapeAmount, shapeSize, offset, ring)
    shapeAmount += 2
    shapeSize += 3
    offset += shapeSize
######


        
# move to the (0, 0) of the cropped page, if you want
translate(bleed, bleed)

saveImage('_exports/04-ring-of-shapes.pdf')