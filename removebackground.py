from rembg import remove
from PIL import Image

input_path = 'pictures/man_with_boxing_costume_and_black_gloves_hd_boxing-1920x1080.jpg'
output_path = 'output.png'

input_image = Image.open(input_path)
output_image = remove(input_image)
output_image.save('output.png')