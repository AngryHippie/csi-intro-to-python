import math

# Dictionary of paint colors and cost per gallon
paintColors = {
    'red': 35,
    'blue': 25,
    'green': 23
}

# FIXME (1): Prompt user to input wall's width
# Calculate and output wall area
wallHeight = float(input('Enter wall height (feet): \n'))
wallWidth = float(input('Enter wall width (feet): \n'))
wallArea = float(wallWidth * wallHeight)
print('Wall area:', wallArea, 'square feet')


# FIXME (2): Calculate and output the amount of paint in gallons needed to paint the wall
paint_needed = wallArea / 350
print('Paint needed:', paint_needed, 'gallons')
# FIXME (3): Calculate and output the number of 1 gallon cans needed to paint the wall, rounded up to nearest integer
cans_needed = math.ceil(paint_needed)
print('Cans needed:', cans_needed, 'can(s) \n')
# FIXME (4): Calculate and output the total cost of paint can needed depending on color
chosen_paint_color = input('Choose a color to paint the wall: \n')
cost_of_paint = paintColors[chosen_paint_color] * cans_needed
print('Cost of purchasing %s paint: $%d' % (chosen_paint_color, cost_of_paint))