# import our function to convert HSV to RGB
from colorsys import hsv_to_rgb

newPage() # make a new page

myShapeCount = 72 # how many shapes to draw

# we can define two variables together, x and y
myFocalPointX, myFocalPointY = 750, 750

strokeWidth(3)
#stroke(1)

# move to our focal point
translate(myFocalPointX, myFocalPointY)

# loop through the number of shapes
for myNumber in range(myShapeCount):
    # figure out hue value
    # myNumber / myShapeCount will give us how far along
    # we are in a single rainbow cycle
    myHueValue = myNumber / myShapeCount
    # use hsv_to_rgb() to get the RGB equivalent
    myRgbColor = hsv_to_rgb(myHueValue, .75, 1)
    # set the fill color
    fill(*myRgbColor)
    # draw the oval, offsetting by the amount of the focal point
    rect(-myFocalPointX, -myFocalPointY, width(), height())
    # change the canvas transformations
    # scale each rectangle down
    scale(.95)
    # rotate each shape
    rotate(18)
    
saveImage('_exports/off-centre-shape.jpg')