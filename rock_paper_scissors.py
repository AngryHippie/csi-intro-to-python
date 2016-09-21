#Rock, Paper, Scissors
#By: Mike Eckrote
#Date: 09/21/16
#
#Credit for me knowing how to generate a random value goes to 'kovshenin' & 'JMSamudio'
#Random generator: http://stackoverflow.com/questions/3996904/generate-random-integers-between-0-and-9
#----------------------------------------------------------------------
#This section declares the variables and imports the "random" module

import random
rock = ['Rock', 'rock', 1, '1']
paper = ['Paper', 'paper', 2, '2']
scissors = ['Scissors', 'scissors', 3, '3']

#----------------------------------------------------------------------
#this section asks for the users input

print('Welcome to Mike\'s crazy game of Rock, Paper, Scissors!')
print('')
print('Think you can beat the computer in this dangerous, dangerous game of life changing choices?')
print('')
print('If you dare proceed, then choose your weapon!!!!')

user_weapon = input('Enter Rock(1), Paper(2), or Scissors(3): ')
print('')

#----------------------------------------------------------------------
#This determines and prints the computers "choice"

computer_weapon = random.randint(1,3)
if computer_weapon in rock:
    print('The computer chose rock')
elif computer_weapon in paper:
    print('The computer chose paper')
elif computer_weapon in scissors:
    print('The computer chose scissors')
else:
    print('something broke')
#----------------------------------------------------------------------

if (user_weapon in rock) and (computer_weapon in rock):
    print('')
    print('tie game...')
if (user_weapon in rock) and (computer_weapon in paper):
    print('')
    print('Paper covers rock, you lose')
if (user_weapon in rock) and (computer_weapon in scissors):
    print('')
    print('Rock smashes scissors, you win!')
#----------------------------------------------------------------------
if (user_weapon in paper) and (computer_weapon in rock):
    print('')
    print('Paper covers rock, you win!')
if (user_weapon in paper) and (computer_weapon in paper):
    print('')
    print('tie game...')
if (user_weapon in paper) and (computer_weapon in scissors):
    print('')
    print('Scissors cut paper, you lose')
# ----------------------------------------------------------------------
if (user_weapon in scissors) and (computer_weapon in rock):
    print('')
    print('Rock smashes scissors, you lose')
if (user_weapon in scissors) and (computer_weapon in paper):
    print('')
    print('Scissors cut paper, you win!')
if (user_weapon in scissors) and (computer_weapon in scissors):
    print('')
    print('tie game...')
# ----------------------------------------------------------------------