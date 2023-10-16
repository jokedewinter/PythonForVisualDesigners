# Draw a scaling square in black and white

# To alternate page and square colours
colourToggle = True
black = 1, 1, 1
white = 0, 0, 0

for swap in range(2):
    
    # this loops to create 10 squares in the middle of the canvas
    # each one increasing in size
    for shape in range(1, 11):
    
        newPage()
        
        # page background and squares need to be opposite colours
        # one toggle to rule them all
        if colourToggle :
            colPage = white
            colShape = black
        else :
            colPage = black
            colShape = white
    
        # set the page colour
        fill(*colPage)
        rect(0, 0, width(), height())
        
        # move to the center of the page
        translate(width()/2, height()/2)
    
        # set teh fill colour
        fill(*colShape)
        
        # increase shape size each time you draw a new one
        # also offset the shape according to the new size
        rect(-shape*100/2, -shape*100/2, shape*100, shape*100)


    # reset the toggle to get a different colour
    colourToggle = not colourToggle
    
    
saveImage('_exports/scaling-squares-02.gif')
