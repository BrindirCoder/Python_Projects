from PIL import Image  # pip install pillow

# Open the input image file
image = Image.open("img.jpg")

# Define the new dimensions (width, height)
new_size = (300, 300)

# Resize the image
resized = image.resize(new_size)

# Save the resized image to a new file
resized.save("resized_image.jpg")

# Confirmation message
print("Image resized successfully!")
