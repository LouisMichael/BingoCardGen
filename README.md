# Process Idea
- make images of each set of numbers, 1 - 75
    - pick a font
        - Font import from PIL in Python: 
        `PIL.ImageFont.truetype(font=None, size=10, index=0, encoding='', layout_engine=None)`
        https://pillow.readthedocs.io/en/stable/reference/ImageFont.html

- Generate a set of numbers
    - 5 in each letter based on the below rules
        - random number between 1 & 15 if already used roll again
        - repeat with an offset for each set

- Do some math to get how big each size each number is as a picture
- Put that pictures into a board so the center of the picture is the center of the grid space

![image of 8.5x11 paper broken into 4x5 boxes](Images\PageLayout.PNG)



# Usage


# Bingo Number Rules
Each space in the 'B' column contains a number from 1 - 15.
Each space in the 'I' column contains a number from 16 - 30.
Each space in the 'N' column contains a number from 31 - 45.
Each space in the 'G' column contains a number from 46 - 60.
Each space in the 'O' column contains a number from 61 - 75.