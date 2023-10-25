# Set a word and give it a wedge shadow
word = "Hello"
offset = 10

newPage()

blendMode('multiply')

fill(random(), random(), random())
fontSize(300)
font('Origin-029-231023-CrazyBlack')


# Display the work in the background first
with savedState() :
    # Straight but slightly offset
    fill(random(), random(), random())
    text(word, (10, 10))

    # Skewed
    fill(random(), random(), random())
    scale(1, .9)
    skew(-10)
    text(word, (0, -10))



# Display the word in black
#fill(0, 0.3)
text(word, (0, offset))


#saveImage('_exports/wedge-word-echo.gif')