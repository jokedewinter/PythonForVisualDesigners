# Draw shapes at random positions on the canvas
# Give them random sizes
# Give them random colours
# Turn it into a little movie/gif

# Set movie length and speed
totalFrames = 10
totalDuration = 5 # seconds


for frame in range(totalFrames):

    newPage()
    frameDuration(totalDuration / totalFrames)

    # Set a white background for the page
    fill(1)
    rect(0, 0, width(), height())

    # Create a lot of blobs
    for step in range(100):
        # Calculate size of shape
        shapeWidth = randint(50, width()/5)
        shapeHeight = randint(50, width()/5)

        # Calculate position of shape
        x = randint(0, width())
        y = randint(0, height())
    
        # Pick a colour
        # Add opacity to make them seethrough
        fill(random(), random(), random(), .7)
        #fill(random(), 0, 0, .5) # Shades of red

        # Draw shape
        oval(x, y, shapeWidth, shapeHeight)


# Save movie
saveImage('_exports/confetti-blobs.gif')
saveImage('_exports/confetti-blobs.png')

