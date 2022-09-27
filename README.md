# Process Idea

- Generate a set of numbers
    - 5 in each letter based on the below rules
        - random number between 1 & 15 if already used roll again
        - repeat with an offset for each set
- layout the gid of numbers, text anchors allow for accurate layout: `d.text((100, 100), "Quick", fill="black", anchor="ms", font=font)`
ref: https://pillow.readthedocs.io/en/stable/handbook/text-anchors.html#text-anchors
    - pick a font
        - Font import from PIL in Python: 
        `PIL.ImageFont.truetype(font=None, size=10, index=0, encoding='', layout_engine=None)`
        https://pillow.readthedocs.io/en/stable/reference/ImageFont.html

- Do some math to get how big each size each number is as a picture
- Put that pictures into a board so the center of the picture is the center of the grid space

![image of 8.5x11 paper broken into 4x5 boxes](.\Images\PageLayout.PNG)



# Usage
py .\MakeDiget.py --font-file bahnschrift.ttf --font-color red --number-of-cards 50

# Bingo Number Rules
Each space in the 'B' column contains a number from 1 - 15.
Each space in the 'I' column contains a number from 16 - 30.
Each space in the 'N' column contains a number from 31 - 45.
Each space in the 'G' column contains a number from 46 - 60.
Each space in the 'O' column contains a number from 61 - 75.
