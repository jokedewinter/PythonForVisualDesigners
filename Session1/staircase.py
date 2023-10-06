# Create a staircase of rectangles
# Pick the colour randomly

columnCount = 10
stepWidth = width()/columnCount

newPage()

# Base colour for the background
fill(randint(0, 1), randint(0, 1), randint(0, 1))
rect(0, 0, width(), height())

# Base colour for the steps
fill(randint(0, 1), randint(0, 1), randint(0, 1))

for step in range(columnCount):
    rect(step*stepWidth, step*stepWidth, stepWidth, height())

saveImage('staircase.png')

