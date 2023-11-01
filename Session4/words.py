# Random word generator

from random import shuffle

wordPath = '/usr/share/dict/words'

# Fonts to use
fonts = ['Origin-031-231029-TextRegular', 'Origin-031-231029-DisplayBlack', 'Origin-031-231029-TextBold', 'Origin-031-231029-CrazyItalicBlack', 'Origin-031-231029-DisplayLight']


# String to print
wordList = FormattedString(
    fontSize = 64,
    align = 'center'
    )


# Set up the page colour
fill(.7, .7, .7)
rect(0, 0, width(), height())

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
margin = 50
contentW = width() - margin * 2
contentH = height() -  margin * 2

textBox(wordList, (margin, margin, contentW, contentH))

saveImage('_exports/words.jpg')