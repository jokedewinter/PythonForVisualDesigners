# Draw a pattern that repeats across the page
# Use a loop to make a grid and draw the columns and rows
# Optional: define functions for the repeats

darkPink = 96/255, 37/255, 53/255 #602535
lightPink = 181/255, 72/255, 100/255 #b54864
green = 117/255, 139/255, 61/255 #758b3d
yellow = 225/255, 205/255, 115/255 #e1cd73
black = 50/255, 50/255, 50/255, .5 #1c1e29
white = 225/255, 213/255, 205/255 #e1d5cd

# Define the block size of your pattern
blockW = 100
blockH = 100

# Define the size of the stripes
stripeHair = 1
stripeSmall = 10
stripeMedium = 30
stripeLarge = 60

newPage(500, 500)

# blendMode('overlay')

# Make a grid
# Loop through rows and colums
# range(start, stop, step)
for y in range(0, height()+blockH, blockH) :
    for x in range(0, width()+blockW, blockW) :
        # fill(random(), random(), random())
        # rect(x, y, blockW, blockH)

        # First fill the big vertical columms
        # Column 1
        fill(*white)
        rect(x, y, stripeMedium, stripeSmall)
        fill(*green)    
        rect(x, y+stripeSmall, stripeMedium, stripeLarge)
        fill(*darkPink)    
        rect(x, y+blockH-stripeMedium, stripeMedium, stripeMedium)        
    
        # Column 2
        fill(*lightPink)
        rect(x+stripeMedium, y, stripeLarge, stripeSmall)
        fill(*yellow)    
        rect(x+stripeMedium, y+stripeSmall, stripeLarge, stripeLarge)
        fill(*green)    
        rect(x+stripeMedium, y+blockH-stripeMedium, stripeLarge, stripeMedium)
        
        # Column 3
        fill(*darkPink)
        rect(x+blockW-stripeSmall, y, stripeSmall, stripeSmall)
        fill(*lightPink)    
        rect(x+blockW-stripeSmall, y+stripeSmall, stripeSmall, stripeLarge)
        fill(*white)    
        rect(x+blockW-stripeSmall, y+blockH-stripeMedium, stripeSmall, stripeMedium)

        # Add the thin black vertical stripes
        fill(*black)
        stripeGap = stripeHair * 3

        # The vertical ones
        stripeStart = (stripeMedium/3*2) + stripeHair
        for stripe in range (0, 7) :
            rect(x+stripeStart, y, stripeHair, height())
            stripeStart += stripeHair + stripeGap

        # The top horizontal ones
        stripeStart = blockH - ((stripeMedium/2*1) + stripeHair)
        for stripe in range (0, 7) :
            rect(x, y+stripeStart, blockW, stripeHair)
            stripeStart -= stripeHair + stripeGap

        # The bottom horizontal ones
        stripeStart = stripeSmall * 2
        for stripe in range (0, 2) :
            rect(x, y+stripeStart, blockW, stripeHair)
            stripeStart -= stripeHair + stripeGap

saveImage('_exports/pattern-normal.jpg')