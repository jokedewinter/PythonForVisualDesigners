# define our constants
inch = 72
cropWidth = 5.83 * inch 
cropHeight = 8.27 * inch
bleed = 0.125 * inch

# do i want to see the bleed?
# NOTE! make this false before exporting
drawBleed = False

# calculate the total width and height
totalWidth = cropWidth+bleed*2
totalHeight = cropHeight+bleed*2

# make a new page
newPage(totalWidth, totalHeight)

with savedState():
    if drawBleed:    
        # draw the crop areas
        stroke(1, 0, 0)
        fill(None)
        strokeWidth(.5)
        rect(bleed, bleed, cropWidth, cropHeight)

###########

    from random import shuffle

    wordPath = '/usr/share/dict/words'
    W = round(width())
    H = round(height())

    # Fonts to use
    fonts = ['Origin-031-231029-TextRegular', 'Origin-031-231029-DisplayBlack', 'Origin-031-231029-TextBold', 'Origin-031-231029-CrazyItalicBlack', 'Origin-031-231029-DisplayLight']

    # String to print
    wordList = FormattedString(
        fontSize = 21,
        align = 'center'
        )


    # Set up the page colour
    fill(.11, .11, .11)
    rect(0, 0, W, H)

    # Read the word file
    with open(wordPath, encoding='utf-8') as wordFile:
        words = wordFile.readlines()
        shuffle(words)
        words = words[:1000] # Use only 1000 words from the list
        i = 0
        for word in words:
            colour = random(), random(), random()
            wordList.append(
                word.strip() + ' ',
                fill = colour,
                font = fonts[i]
                )
            i += 1
            if i > 4 :
                i = 0

    # Put it on the page
    margin = 10
    contentW = W - margin * 2
    contentH = H -  margin * 2

    textBox(wordList, (margin, margin, contentW, contentH))

##########

        
# move to the (0, 0) of the cropped page, if you want
translate(bleed, bleed)

saveImage('_exports/05-words.jpg')