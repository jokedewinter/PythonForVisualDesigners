# Pixelate an image and then clean it up
imageName = '_assets/bridge.jpg'
imFish = ImageObject(imageName)
xCount, yCount = 50, 50
multiplier = .2
frames = 10

for phase in range(2) :
    for frame in range(frames) :
        newPage(*imFish.size())
        cellW, cellH = width()/xCount, height()/yCount

        for row in range(yCount) :
            for col in range(xCount) :
                x = cellW * col
                y = cellH * row
                colour = imagePixelColor(imFish, (x, y))
                fill(*colour)
                rect(x, y, cellW, cellH)

        xCount = int(xCount + xCount * multiplier)
        yCount = int(yCount + yCount * multiplier)
    
    multiplier = -multiplier

    
saveImage('_exports/filter-pixelate.gif')