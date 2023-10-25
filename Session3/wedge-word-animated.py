# Set a word and give it a wedge shadow
word = "Hello"

for frame in range(50) :
    newPage(1000, 500)

    blendMode('multiply')

    fill(random(), random(), random())
    fontSize(300)
    font('Origin-029-231023-CrazyBlack')

    # Go to center of canvas
    translate(width()/2, height()/3)


    # Display the work in the background first
    with savedState() :
        # Straight but slightly offset
        fill(random(), random(), random())
        text(word, (10, 10), align="center")
    
        # Skewed
        fill(random(), random(), random())
        scale(1, .9)
        skew(-10)
        text(word, (0, -10), align="center")
    


    # Display the word in black
    #fill(0, 0.3)
    text(word, (0, 0), align="center")


saveImage('_exports/wedge-word-animated.gif')