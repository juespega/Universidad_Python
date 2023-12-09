"""
Instructions:
- In the following exercise you are asked to calculate the area and perimeter
of a rectangle, to do this we must create the following variables:

high(int)
width(int)

- The user must provide the height and width values, and then
The result must be printed in the following format:
(do not use accents and respect spaces, uppercase, lowercase and breaks
line)

Provide the height of the rectangle:
Provide the width of the rectangle:
Area: <area>
Perimeter: <perimeter>

Formulas:
Area: height * width
Perimeter: (height + width) * 2
"""

height = int(input('Provide the height of the rectangle :')) 
width = int(input('Provide the width of the rectangle: '))
print (f'Area: {height * width}')
print (f'Perimeter: {(width * height) * 2}')