# Vasarely black and white squares

cube = (width() - 100) / 11
print(cube, width(), cube*11+100)

for frame in range(4) :
    
    newPage()
    translate(0, 50)
    for row in range(11) :
        with savedState() :
            
            translate(50, 0)
            
            for column in range (11):

                if row in range(1, 8) :
                    rotate(-(column+row)*2)
                    rect(0, 0, cube*.8, cube*.8)
                    rotate((column+row)*2)
                else :
                    rect(0, 0, cube*.8, cube*.8)
                    
                translate(cube, 0)
        translate(0, cube)
