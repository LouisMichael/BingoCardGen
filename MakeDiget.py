#!/usr/bin/env python
from PIL import Image, ImageFont, ImageDraw
import argparse

# Create 300 pixel per inch PNG for the numbers 1 - 75 in the front specified by the user
def main(fontFile):


    W, H = (180,180)
    msg = "1"

    im = Image.new("RGBA",(W,H),"white")
    draw = ImageDraw.Draw(im)
    draw.textbbox((0,0), msg, font=font, anchor=None, spacing=4, align='left', direction=None, features=None, language=None, stroke_width=0, embedded_color=False)
    w, h = draw.textsize(msg)
    print(f"width of text: {w} height of text: {h}")
    font = ImageFont.truetype("arial.ttf", 10)

    draw.text(((W-w)/2,(H-h)/2), msg, fill="black", font=font)
    im.save("hello.png", "PNG")


parser = argparse.ArgumentParser(description='given a font output PNG of the numbers 1-75 in this font')
parser.add_argument('--font-file', help='path to a font file', required=False,
  dest='fontFile')

args = parser.parse_args()
# Here we go!
main(args.fontFile)
