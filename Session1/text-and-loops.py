# A string of text scattered over the page
# The loop creates multiple pages you can save as a gif/movie to make it animated

myString = 'hello world'

for myPage in range(10):
    newPage()
    rect(0, 0, width(), height())
    for myLetter in myString:
        x = randint(0, width())
        y = randint(0, height())
        fontSize(50)
        fill(random(), random(), random())
        text(myLetter, (x, y))

#saveImage('_exports/letters'+str(myPage)+'.png')
saveImage('_exports/movie.gif')