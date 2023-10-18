
# prints in the console
print('Hello world')

# prints on the canvas at the bottom left
fontSize(100)
font('Verdana')
fill(1, 0, 0)
fill(55/255, 105/255, 204/255)
text('Hello world', (0, 0))

# prints all the installed fonts on your computer
print(len(installedFonts()))
print(installedFonts())