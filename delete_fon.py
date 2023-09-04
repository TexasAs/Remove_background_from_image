from rembg import remove
from PIL import Image


input_image_path = 'Your path'           # Path to original image
output_image_path = 'output_image.png'   # Path to save image

image = Image.open(input_image_path)
output = remove(image)

output.save(output_image_path)

