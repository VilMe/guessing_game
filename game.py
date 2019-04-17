"""A number-guessing game."""
from random import randint

# Put your code here
print('Hi!')
player_name = input('What is you name? ') 
our_number = randint(0,100)
player_num = int(input('Guess a number between 1 and 100: '))
number_of_guesses = 1

if 1 <= player_num <= 100:
    while player_num != our_number:
        if player_num > our_number:
            player_num = int(input('Too high! Guess another number: '))
            number_of_guesses += 1
        elif player_num < our_number:
            player_num = int(input('Too low! Guess another number: '))
            number_of_guesses += 1
    print(player_name + ' you got my number! In only ' + str(number_of_guesses) + ' guesses!')
else:
    print("that number ain't between 1 and 100, guess again")
    continue
