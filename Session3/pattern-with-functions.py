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

def stripe(colour, x, y, sizeW, sizeH) :
    fill(*colour)
    rect(x, y, sizeW, sizeH)

newPage(500, 500)

#blendMode('overlay')

# Make a grid
# Loop through rows and colums
# range(start, stop, step)
for y in range(0, height()+blockH, blockH) :
    for x in range(0, width()+blockW, blockW) :
        # fill(random(), random(), random())
        # rect(x, y, blockW, blockH)

        # First fill the big vertical columms
        # Column 1
        stripe(white, x, y, stripeMedium, stripeSmall)
        stripe(green, x, y+stripeSmall, stripeMedium, stripeLarge)
        stripe(darkPink, x, y+blockH-stripeMedium, stripeMedium, stripeMedium)        
    
        # Column 2
        stripe(lightPink, x+stripeMedium, y, stripeLarge, stripeSmall)
        stripe(yellow, x+stripeMedium, y+stripeSmall, stripeLarge, stripeLarge)
        stripe(green, x+stripeMedium, y+blockH-stripeMedium, stripeLarge, stripeMedium)
        
        # Column 3
        stripe(darkPink, x+blockW-stripeSmall, y, stripeSmall, stripeSmall)
        stripe(lightPink, x+blockW-stripeSmall, y+stripeSmall, stripeSmall, stripeLarge)
        stripe(white, x+blockW-stripeSmall, y+blockH-stripeMedium, stripeSmall, stripeMedium)

        # Add the thin black vertical stripes
        colour = black
        stripeGap = stripeHair * 3

        # The vertical ones
        stripeStart = (stripeMedium/3*2) + stripeHair
        for z in range (0, 7) :
            stripe(colour, x+stripeStart, y, stripeHair, height())
            stripeStart += stripeHair + stripeGap

        # The top horizontal ones
        stripeStart = blockH - ((stripeMedium/2*1) + stripeHair)
        for z in range (0, 7) :
            stripe(colour, x, y+stripeStart, blockW, stripeHair)
            stripeStart -= stripeHair + stripeGap

        # The bottom horizontal ones
        stripeStart = stripeSmall * 2
        for z in range (0, 2) :
            stripe(colour, x, y+stripeStart, blockW, stripeHair)
            stripeStart -= stripeHair + stripeGap

# saveImage('_exports/pattern-colours.jpg')