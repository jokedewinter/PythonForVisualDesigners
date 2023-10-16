# Draw a ring of circles in the center of the canvas 
# using translate() and rotate()

circle = 350
amount = 15

# will make the coloured circle transparentish
blendMode('overlay')

# move to the center of the page
translate(width()/2, height()/2)

# loop through amount of shapes to draw
for thing in range(amount):
    
    # set a colour
    # the opacity value helps with the blendmode
    fill(random(), random(), random(), 0.5)
    # offset the circle a little
    oval(circle/4, -circle/4, circle, circle)  
    # rotate the canvas to get a new point to start from 
    rotate(360/amount)

    
saveImage('_exports/ring-of-circles.jpg')
