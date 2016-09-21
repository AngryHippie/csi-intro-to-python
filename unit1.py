#Writen by: Michael Eckrote
#
# This program is going to accept some input about distance and
# time, and will use that info to determine all sorts of cool things!

# This container hold how many feet are in various distances
distance_key_feet = {
    'inch': 1/12, 'Inch': 1/12, 'inches': 1/12, 'Inches': 1/12,
    'Feet': 1, 'feet': 1, 'foot': 1, 'Foot': 1,
    'yard': 3, 'Yard': 3, 'yards': 3, 'Yards': 3,
    'Mile': 5280, 'mile': 5280, 'Miles': 5280, 'miles': 5280,
    'kilometers': 3280.84, 'Kilometers': 3280.84, 'kilometer': 3280.84,'Kilometer': 3280.84,
    'meter': 3.28084, 'Meter': 3.28084, 'meters': 3.28084, 'Meters': 3.28084,
    'centimeter': 0.0328084, 'Centimeter': 0.0328084, 'centimeters': 0.0328084, 'Centimeters': 0.0328084,
    'millimeter': 0.00328084, 'Millimeter': 0.00328084, 'Millimeters': 0.00328084, 'millimeters': 0.00328084
}

# This container holds how many hours are in various units of time
time_key_hours = {
    'seconds': 0.000277778, 'Seconds': 0.000277778, 'second': 0.000277778, 'Second': 0.000277778, 'sec': 0.000277778, 'secs': 0.000277778, 'Sec': 0.000277778, 'Secs': 0.000277778,
    'minutes': 0.0166667, 'Minutes': 0.0166667, 'minute': 0.0166667, 'Minute': 0.0166667, 'min': 0.0166667, 'Min': 0.0166667, 'mins': 0.0166667, 'Mins': 0.0166667,
    'hour': 1, 'Hour': 1, 'hours': 1, 'Hours': 1,
    'day': 24, 'Day': 24, 'days': 24, 'Days': 24,
    'year': 8760, 'Year': 8760, 'years': 8760, 'Years': 8760
}

# The section asks the user for all the required info (5 prompts)

# 1
chosen_location = input(
    'Think of a location you travel\n'
    'to every day; preferable somewhere\n'
    'close like work or school:\n'
    ''
)
print('')

#2
distance_to_location = float(input(
    'Enter the distance you travel\n'
    'going to %s in whatever unit of\n'
    'measurement that you want (numbers only):\n'
    '' % chosen_location
))
print('')

#3
chosen_unit_of_distance = input(
    'Enter the unit of distance you chose\n'
    'ex - miles, feet, kilometers:\n'
    ''
)
print('')

#4
time_to_location = float(input(
    'Enter the time it takes to travel\n'
    'to %s in whatever unit of measurement\n'
    'that you want (numbers only):\n'
    '' % chosen_location
))
print('')

#5
chosen_unit_of_time = input(
    'Enter the unit of time you chose\n'
    'ex- seconds, minutes, hours:\n'
    ''
)
print('')

# These next 2 lines convert any input into miles and hours, and then MPH
distance_to_location_in_miles = (distance_key_feet[chosen_unit_of_distance] * distance_to_location) / 5280
time_to_location_in_hours = time_key_hours[chosen_unit_of_time] * time_to_location
mph_to_location = distance_to_location_in_miles / time_to_location_in_hours
days_to_the_moon = (238900 / mph_to_location) / 24
days_to_mars = (33900000 / mph_to_location) / 24

print('%s is %s miles from your home' % (chosen_location, distance_to_location_in_miles))
print('')
print('it takes you %s hours to get there' %time_to_location_in_hours)
print('')
print('you travel to %s at an average speed of %s mph' %(chosen_location, mph_to_location))
print('')
print('it would take you %s days to travel to the moon at that speed,' % days_to_the_moon)
print('and %s days to get to mars!' % days_to_mars)

