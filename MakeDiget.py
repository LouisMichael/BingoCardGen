#!/usr/bin/env python
from PIL import Image, ImageFont, ImageDraw
import argparse
import random
# Create 300 pixel per inch PNG for the numbers 1 - 75 in the front specified by the user
def main(fontFile, fontColor, templateFile, numberOfCards, cardDestination):
    for cardNumber in range(numberOfCards):
        values = []
        for i in range(5):
            values.append([])
            for j in range(5):
                # print(f"i: {i} j:{j}")
                candidate = random.randint((i*15)+1,(i*15)+15)
                # print(f"candidate first roll: {candidate}")

                while(candidate in values[i]):
                    candidate = random.randint((i*15)+1,(i*15)+15)
                    # print(f"candidate reRoll: {candidate}")
                values[i].append(candidate)
                # print(f"candidate used: {candidate}")

        # one square will be .6 in x .6 in at 300 pixels per inch this is 180 x 180
        W, H = (180*5,180*5)
        im = Image.new("RGBA",(W,H),None)
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype(fontFile, 50)

    

        # draw.textbbox((0,0), msg, font=font, anchor=None, spacing=4, align='left', direction=None, features=None, language=None, stroke_width=0, embedded_color=False)
        # future perfect vertical alignment could be achieved with textbbox sizeing
        # w, h = draw.textsize(msg)
        # print(f"width of text: {w} height of text: {h}")

        for i in range(5):
            for j in range(5):
                draw.text((90 + (i*180),90+(j*180)), f"{values[i][j]}", fill=fontColor, anchor="mm", font=font)

        # lines from top to bottom
        for i in range(4):
            draw.line(((180*(i+1), 0), (180*(i+1), 180*5)), fontColor)
        for i in range(4):
            draw.line(((0, 180*(i+1)), (180*5, 180*(i+1))), fontColor)
        background = Image.open(templateFile)
        foreground = im

        # .5 in x 1.5 in offset, see layout image for visual
        background.paste(foreground, (150, 450), foreground)
        background.save(f"{cardDestination}/{cardNumber}.png", "PNG")


parser = argparse.ArgumentParser(description='given a font output PNG of a grid of bingo numbers')
parser.add_argument('--font-file', help='path to a font file', required=False,
  dest='fontFile', default='arial.ttf')
parser.add_argument('--font-color', help='font color', required=False,
  dest='fontColor', default='black')
parser.add_argument('--template-file', help='the path to a 1200px X 1500px png file that will be used as the template for the cards', required=False,
  dest='templateFile', default='./Images/exampleTemplate.png')
parser.add_argument('--number-of-cards', type=int, help='the number of cards you want to make', required=False,
  dest='numberOfCards', default=1)
parser.add_argument('--card-destination', help='the file path to put cards', required=False,
  dest='cardDestination', default='./CardsOut')

args = parser.parse_args()
# Here we go!
main(args.fontFile, args.fontColor, args.templateFile, args.numberOfCards, args.cardDestination)
