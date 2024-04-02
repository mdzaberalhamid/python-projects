# Project 21 
# Image Resizer

# Step 1 - install pillow if you haven't 
# Step 2 - import pillow
# Step 3 - open up the image we want to resize using python
# Step 4 - print the current size of that image
# Step 5 - specify the size we want to change it to
# Step 6 - save the new resized image

from PIL import Image

print('Image Resizer\n')

image = Image.open('qrimg.png')

print(f"Current image size: {image.size}")

resized_image = image.resize((500, 500))

resized_image.save('qrimg-500.png')

# Continuing...
