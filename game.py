"""A number-guessing game."""
from random import randint

# Put your code here
print('Hi!')
player_name = input('What is you name? ') 
our_number = randint(0,100)
player_num = int(input('Guess a number between 1 and 100: '))
while player_num != our_number:
    if player_num > our_number:
        player_num = int(input('Too high! Guess another number: '))
        continue
    elif player_num < our_number:
        player_num = int(input('Too low! Guess another number: '))
        continue

print(player_name + ' you won!')
