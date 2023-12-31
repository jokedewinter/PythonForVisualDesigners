# Make a donut shape in the middle of the page
# Make the shape responsive to the size of the canvas

# Optional: I have centered the shape

newPage()
# Create a white canvas
fill(1)
rect(0, 0, width(), height())
# Make the outside shape
fill(0)
oval(width()/20/2, height()/20/2, width()-(width()/20), height()-(height()/20))
# Make the inside shape
fill(1)
oval(width()/4, height()/4, width()/2, height()/2)

saveImage('donut.png')


# Alternative
# # define the thickness of the donut
# thickness = 300

# # draw a big circle on the outside, make it black
# # use width() and height() to make the circle the full size of the page
# fill(0)
# oval(0, 0, width(), height())

# # now draw a smaller white circle on top of it
# fill(1)
# # the x and y will both offset by the thickness value
# # for the width and height, we have to do a little math
# # the width inner circle is equal to the full width minus the thicnkess of both sides of the donut
# # same for height
# oval(thickness, thickness, width()-thickness*2, height()-thickness*2)

