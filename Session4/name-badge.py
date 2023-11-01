# Design a sheet of business cards based on a spreadsheet

import csv

attendee = random(), random(), random()
speaker = random(), random(), random()
organiser = random(), random(), random()

def getRandomCoords(startPoint, endPoint) :
    return randint(startPoint, endPoint)



def drawCard(row, boxSize) :
    currentX, currentY, cardWidth, cardHeight = boxSize
    
    with savedState() :
        # Position to the current card location
        translate(currentX, currentY)
        with savedState() :
            lineDash(2)
            fill(None)
            stroke(.9)
            rect(0, 0, cardWidth, cardHeight)
        translate(0, 0)

        # Give the card a colour depending on role
        colour = speaker
        if 'Attendee' == role :
            colour = attendee
        elif 'Organiser' == role :
            colour = organiser
        fill(*colour, .6)
        rect(0, 0, cardWidth, cardHeight)

        shapeWidth = cardWidth/3*1.5
        shapeHeight = cardHeight

        # Add some wild shapes
        wild = BezierPath()        
        for wildThing in range(5) :
            wild.moveTo((getRandomCoords(0, shapeWidth), getRandomCoords(0, shapeWidth)))
    
            wild.curveTo(
                (getRandomCoords(0, shapeWidth), getRandomCoords(0, shapeWidth)), # handle 1
                (getRandomCoords(0, shapeWidth), getRandomCoords(0, shapeWidth)), # handle 2
                (getRandomCoords(0, shapeWidth), getRandomCoords(0, shapeWidth))  # on curve point
             )
        fill(.1, .7)
        drawPath(wild)

        # Person
        personName = FormattedString(
            name,
            font = 'Origin-032-231031-DisplayBlack',
            fontSize = 20,
            lineHeight = 15,
            fill = 1           
            )
        textBox(personName, (cardWidth/3, cardHeight-90, cardWidth-100, cardHeight-100))
    
        # Draw a background for the remaining blurb
        # But only if there is blurb
        if "" != affiliation :
            fill(*colour, .8)
            rect(cardWidth/3-5, cardHeight-125, cardWidth-100, cardHeight-100)
        
        # Affiliation
        personAffl = FormattedString(
            affiliation, 
            font = 'Origin-031-231029-TextRegular',
            fontSize = 9,
            lineHeight = 15,
            fill = 0           
            )
        textBox(personAffl, (cardWidth/3, cardHeight-130, cardWidth-100, cardHeight-100))
    
        # Role
        personRole = FormattedString(
            role.upper(),
            font = 'Origin-031-231029-TextBold',
            fontSize = 10,
            lineHeight = 15,
            fill = (1)           
           )
        textBox(personRole, (cardWidth/3, cardHeight-145, cardWidth-100, cardHeight-100))
    
    
    
    
    
##############################

# Set the page size for the contact sheet of cards
newPage('A4')

# Set the size of the cards
inch = 72
cardWidth = inch * 3.5 #252
cardHeight = inch * 2 #144

# Calculate how many cards fit on a page
perRow = int(width() / cardWidth)
perCol = int(height() / cardHeight)

# Center the cards on the page
paperMarginX = (width() - cardWidth * perRow) / 2
paperMarginY = (height() - cardHeight * perCol) / 2
currentX = paperMarginX
currentY = paperMarginY

# Crappy work around to avoid a blank page being added to the end
with open ('_assets/FantasyConference.csv', encoding='utf-8') as countFile:
    peopleList = csv.reader(countFile)
    countPeople = len(list(peopleList))
    
# Open csv file
with open ('_assets/FantasyConference.csv', encoding='utf-8') as csvFile:
    people = csv.reader(csvFile)

    # Loop throught the rows,
    # but skip over the first row (title row)
    for index, row in enumerate(people) :  

        if index == 0 :
            continue
        
        # Assign the columns to variables
        name, affiliation, role = row

        # Create a card for this person
        drawCard(row, (currentX, currentY, cardWidth, cardHeight))

        # Move to the next card, but not if you've run out of space
        currentX += cardWidth
        
        if currentX + cardWidth > width() :
            currentX = paperMarginX
            currentY += cardHeight
            
            # Check if you're running out of space on the page as well 
            # If yes, start a new page
            if (currentY + cardHeight > height()) and (index < countPeople-1) :
                newPage('A4')
                currentY = paperMarginY
        

#saveImage('_exports/business-cards.pdf')        
