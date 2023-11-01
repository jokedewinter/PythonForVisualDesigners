# Draw shapes at random positions on the canvase
# Give them random colours

# Set shape dimensions
shapeWidth = 27
shapeHeight = 27

# Circles
newPage()
fill(1)
rect(0, 0, width(), height())

for step in range(1000):
    # Determine position of shape
    x = randint(0, width())
    y = randint(0, height())
    # Pick a colour
    fill(random(), random(), random())
    # Draw the shape
    oval(x, y, shapeWidth, shapeHeight)

#saveImage('_exports/confetti-circles.png')

# Squares
newPage()
fill(1)
rect(0, 0, width(), height())

for step in range(1000):
    x = randint(0, width())
    y = randint(0, height())
    fill(random(), random(), random())
    rect(x, y, shapeWidth, shapeHeight)

#saveImage('_exports/confetti-squares.png')

# Circles and squares
newPage()
fill(1)
rect(0, 0, width(), height())

for step in range(500):
    x = randint(0, width())
    y = randint(0, height())
    fill(random(), random(), random())
    oval(x, y, shapeWidth, shapeHeight)
    # Draw a different shape
    x = randint(0, width())
    y = randint(0, height())
    rect(x, y, shapeWidth, shapeHeight)

#saveImage('_exports/confetti-mix.png')


# Circles with different sizes
newPage()
fill(1)
rect(0, 0, width(), height())

for step in range(500):
    # Determine the size of the shape
    shapeWidth = randint(10, width()/10)
    shapeHeight = randint(10, height()/10)
    
    # Determine position of shape
    x = randint(0, width())
    y = randint(0, height())
    # Pick a colour
    opacity = (shapeWidth/width())*10
    fill(random(), random(), random(), opacity)
    # Draw the shape
    oval(x, y, shapeWidth, shapeHeight)

#saveImage('_exports/confetti-sizes.png')
