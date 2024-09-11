#! /usr/local/bin/python3

import sys
import random

def welcome_section():
    print('Welcome to the Number Guessing Game!')
    print('I\'m thinking of a number between 1 and 100.')
    print('You have 5 chances to guess the correct number.')

    print('Please select the difficulty level:')
    print("1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)")

def select_difficulty():
    number_of_attemps = 0
    level = ''
    selected = False

    while not selected:
        d = input('Enter your choice: ')

        match(d):
            case '1':
                level = 'Easy'
                number_of_attemps = 10
                selected = True
            case '2':
                level = 'Medium'
                number_of_attemps = 5
                selected = True
            case '3':
                level = 'Hard'
                number_of_attemps = 3
                selected = True
            case 's':
                sys.exit()
            case _:
                print('Please select a valid value or introduce \'s\' if you want to exit the game.')

    print(f'Great! You have selected the {level} difficulty level.')
    return number_of_attemps

def playing(number_of_attemps) -> bool:
    attemps = 0
    number = random.randint(1, 100)
    
    print('Let\'s start the game!\n')

    while attemps < number_of_attemps:
        input_guess = input('Enter your guess: ')
        if input_guess == 's':
            sys.exit()

        try: 
            attemps = attemps + 1
            number_selected = int(input_guess)
        except: 
            print('Please introduce a valid value or introduce \'s\' if you want to exit the game.\n')
            continue
        
        if number == number_selected:
            return attemps, True
        elif number < number_selected:
            print(f'Incorrect! The number is less than {number_selected}.\n')
        else:
            print(f'Incorrect! The number is greater than {number_selected}.\n')

    return attemps, False

def main():
    welcome_section()
    number_of_attemps = select_difficulty()
    attemps, win = playing(number_of_attemps)

    if win:
        print(f'Congratulations! You guessed the correct number in {attemps} attempts.')
    else:
        print(f'Failed! You didn\'t guess the number in {attemps} attempts.')
        
if __name__ == '__main__':
    main()