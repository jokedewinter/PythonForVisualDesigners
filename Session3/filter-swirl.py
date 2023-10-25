# Do some funny stuff with an image

imageName = '_assets/snow.jpg'
imSnow = ImageObject(imageName)

# Create a page the size of the image
newPage(*imSnow.size())

# Some stuff
imSnow.sepiaTone(3)
imWidth, imHeight = imSnow.size()
center = (imWidth/2, imHeight/2)
imSnow.twirlDistortion(center, width()/2.5)

image(imSnow, (0, 0))

saveImage('_exports/filter-swirl.jpg')