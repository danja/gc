import numpy as np
from PIL import Image, ImageDraw

# Define the room dimensions
room_size = 16

# Create a new image with a white background
img = Image.new('RGB', (room_size*16, room_size*16), (255, 255, 255))
draw = ImageDraw.Draw(img)

# Draw ice blocks
ice_color = (173, 216, 230)  # Light blue
for x in range(room_size):
    for y in range(room_size):
        draw.rectangle([(x*16, y*16), ((x+1)*16-1, (y+1)*16-1)],
                       fill=ice_color, outline=(255, 255, 255))

# Draw door
door_color = (139, 69, 19)  # Brown
draw.rectangle([(room_size*16//4, room_size*16//2),
               (room_size*16//4 + 16, room_size*16//2 + 32)], fill=door_color)

# Draw St. Bernard
dog_color = (245, 222, 179)  # Light brown
draw.ellipse([(room_size*16//4 + 4, room_size*16//2 + 8),
             (room_size*16//4 + 12, room_size*16//2 + 16)], fill=dog_color)

# Draw angry goat
goat_color = (210, 105, 30)  # Brown
draw.rectangle(
    [(room_size*16 - 16, 0), (room_size*16 - 32, 16)], fill=goat_color)
draw.ellipse([(room_size*16 - 24, 16), (room_size*16 - 16, 24)],
             fill=goat_color)

# Draw frozen waterfall
waterfall_color = (135, 206, 235)  # Light blue
draw.rectangle([(room_size*16 - 32, room_size*16//2),
               (room_size*16, room_size*16)], fill=waterfall_color)

# Save the image
img.save('ice_platform_room.png')
