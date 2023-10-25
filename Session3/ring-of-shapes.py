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
     

ringsTotal = 27
shapeSize = 5
shapeAmount = 21
offset = 6  
    
newPage()

# Set background colour
fill(1)
rect(0, 0, width(), height())
    
# Move to the center of the page
translate(width()/2, height()/2)

# Loop throught the amount of rings
for ring in range(ringsTotal) :
    
    fill(random(), random(), random())
    circleShapes(shapeAmount, shapeSize, offset, ring)
    shapeAmount += 3
    shapeSize += 5
    offset += shapeSize
    
saveImage('_exports/ring-of-shapes.jpg')