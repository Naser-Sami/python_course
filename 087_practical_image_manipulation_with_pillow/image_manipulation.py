# -------------------------------------------------
# -- Practical => Image Manipulation With Pillow --
# -------------------------------------------------

from PIL import Image


# Open The Image
myImage = Image.open("/Users/naserebedo/Pictures/FC9D4058-DC48-4728-A39B-9172F57E4442_4_5005_c.jpeg")

# Show The Image
# myImage.show()

# My Cropped Image
myBox = (300, 300, 800, 800)
myNewImage = myImage.crop(myBox)

# Show The New Image
# myNewImage.show()

# My Converted Mode Image
myConverted = myImage.convert("L")
myConverted.show()
