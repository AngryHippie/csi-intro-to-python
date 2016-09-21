# Unit 2 Calculator
# By: Mike Eckrote
# Date: 09/21/16
#
# Description: This calculator will perform the 4 basic math operations
#   Addition, Subtraction, Multiplication, & Division
#


#
print('Mike\'s Magical Calculator!')
print('')

#Possible Operations:
addition_operations = {'Add':'+','add':'+','Plus':'+','plus':'+','addition':'+','Addition':'+', '+': '+'}
subtraction_operations = {'Subtract': '-','subtract':'-','Minus':'-','minus':'-','Subtraction':'-','subtraction':'-',
                          '-': '-'}
multiplication_operations = {'Multiply': '*','multiply':'*','Times':'*','times':'*','Multiplication':'*',
                             'multiplication':'*', '*': '*'}
division_operations = {'Divide': '/','divide':'/','Division':'/','division':'/', '/': '/'}

#User selects desired operation:
print('Would you like to add, subtract, multiply, or divide?')
operation = input('Desired operation --> ')

if operation in addition_operations:
    first_number = float(input('Enter the first number you want to add: '))
    second_number = float(input('Enter the number you would like to add to %f: ' %first_number))
    print('')
    print('%f %s %f =' % (first_number, addition_operations[operation], second_number),
          (first_number + second_number))
elif operation in subtraction_operations:
    first_number = float(input('Enter the first number you want to subtract: '))
    second_number = float(input('Enter the number you would like to subtract from %f: ' %first_number))
    print('')
    print('%f %s %f =' % (first_number, subtraction_operations[operation], second_number),
          (first_number - second_number))
elif operation in multiplication_operations:
    first_number = float(input('Enter the first number you want to multiply: '))
    second_number = float(input('Enter the number you would like to multiply %f by: ' %first_number))
    print('')
    print('%f %s %f =' % (first_number, multiplication_operations[operation], second_number),
          (first_number * second_number))
elif operation in division_operations:
    first_number = float(input('Enter the first number you want to divide: '))
    second_number = float(input('Enter the number you would like to divide %f by: ' %first_number))
    print('')
    print('%f %s %f =' % (first_number, division_operations[operation], second_number),
          (first_number / second_number))
else:
    print('')
    print('Error: That is not a known operation, please re-run this program')
    quit()