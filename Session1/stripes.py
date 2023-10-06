# Create a series of rectangles with a gradient from red, green or blue
# Pick the colour randomly

columnCount = 10
stepWidth = width()/columnCount

# Colours go gradually darker, sometimes all black
newPage()

baseRed = randint(0, 1)
baseGreen = randint(0, 1)
baseBlue = randint(0, 1)
fill(baseRed, baseGreen, baseBlue)

for step in range(columnCount):
    fill(baseRed/(step+1), baseGreen/(step+1), baseBlue/(step+1))
    rect(step*stepWidth, 0, stepWidth, height())

saveImage('stripes-darker.png')


# Colours become lighter all the way to white
newPage()

baseRed = randint(0, 1)
baseGreen = randint(0, 1)
baseBlue = randint(0, 1)
fill(baseRed, baseGreen, baseBlue)

for step in range(columnCount):
    baseRed += 1/columnCount
    baseGreen += 1/columnCount
    baseBlue += 1/columnCount
    fill(baseRed, baseGreen, baseBlue)
    rect(step*stepWidth, 0, stepWidth, height())

saveImage('stripes-lighter.png')

# Colours become gradually lighter from red to yellow
newPage()

baseRed = 1
baseGreen = 0
baseBlue = 0

for step in range(columnCount):
    fill(baseRed, baseGreen, baseBlue)
    rect(step*stepWidth, 0, stepWidth, height())
    baseGreen += 1/columnCount


saveImage('stripes.png')