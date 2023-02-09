from football_data import get_table
from PIL import Image, ImageDraw, ImageFont

def draw_table(code):
    text = get_table(code)
    image = Image.open('files\paper.jpeg')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('roboto.ttf', 40)
    draw.text((20, 20), text, (0, 0 , 0), font = font)
    image.save('files\comp_table.jpeg')

draw_table('fl')