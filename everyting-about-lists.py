#--------------------------------------------------------------------------------------------
#Dictionairy overview
#--------------------------------------------------------------------------------------------

test_scores = {
    'Deb': 89,
    'Fred' : 73,
    'Ted' : 66
}

print(test_scores)

#--------------------------------------------------------------------------------------------
#adding values to a dictionary:
#--------------------------------------------------------------------------------------------

test_scores['Geb'] = 23

print(test_scores)

#--------------------------------------------------------------------------------------------
#updating existing values (more along the lines of replacing existing values)
#--------------------------------------------------------------------------------------------

test_scores['Geb'] = 93

print(test_scores)

#--------------------------------------------------------------------------------------------
#removing existing entries
#--------------------------------------------------------------------------------------------

del test_scores['Ted']

print(test_scores)

#--------------------------------------------------------------------------------------------
print('')
#--------------------------------------------------------------------------------------------
print('')
#--------------------------------------------------------------------------------------------
#Tuple Overview: Same as list but immutable
#--------------------------------------------------------------------------------------------

white_house_coordinates = (38.8977, 77.0366)

print(white_house_coordinates)

#--------------------------------------------------------------------------------------------
#Sequencing functions:
#--------------------------------------------------------------------------------------------

print('number of items in the list: ', len(white_house_coordinates))

a_random_few_numbers = (7684, 69)

weird_tuple = white_house_coordinates + a_random_few_numbers

print(weird_tuple)
print('min value:', min(weird_tuple))
print('max value:', max(weird_tuple))
print('sum of value:', sum(weird_tuple))
print('index that 7684 resides in:', weird_tuple.index(7684))
print('number of times 69 is listed: ', weird_tuple.count(69))

#--------------------------------------------------------------------------------------------
print('')
#--------------------------------------------------------------------------------------------
print('')
#--------------------------------------------------------------------------------------------
#Lists Overview: same as "Tuple" but with a few extra features (mutable)
#--------------------------------------------------------------------------------------------

random_list = [45, 66, 79, 69, 23, 34, 73, 51]

print(random_list)

#--------------------------------------------------------------------------------------------
# list can use all the same min/max/sum commands that tuple can with the addition of:
#--------------------------------------------------------------------------------------------

random_list.append(55)

print('I just added 55 to the end of the list:', random_list)

random_list.pop(3)
print('I just removed the 4th item from the list (index 3)', random_list)

random_list.remove(73)

print('I just removed the number 73 from the list:', random_list)


#this is a change
