# Draw concentric circles that alternate between a random color and white

# To alternate page and square colours
colourToggle = True

# Shape size
size = width()*2

for swap in range(2):

    newPage()

    # move to the center of the page
    translate(width()/2, height()/2)

    for shape in range(50):
        
        # Alternate circle colour between random and white
        if colourToggle :
            fill(random(), random(), random())
        else :
            fill(1)

        oval(-size/2, -size/2, size, size)
        
        # scale canvas so that you don't have to resize the shape
        scale(0.9)

        # reset the toggle to get a different colour
        colourToggle = not colourToggle

saveImage('_exports/concentric-circles-01.gif')
