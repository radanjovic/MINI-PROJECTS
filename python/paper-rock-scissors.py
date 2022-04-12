# Implementation of rock, paper, scissors game
import random

# Possible options
options = ['rock', 'paper', 'scissors']

# Creating game
def game():
    # Getting inputs
    user_input = input('Enter: paper, rock or scissors: ').lower()
    computer_input = options[random.randint(0,2)]

    # Check validity and get results
    if user_input in options:
        print('You typed in: ' + user_input)
        print('Computer selected: ' + computer_input)
        if user_input == 'rock':
            if computer_input == 'rock':
                print('Tie!')
            elif computer_input == 'paper':
                print('Computer wins!')
            elif computer_input == 'scissors':
                print('You win!')
        if user_input == 'paper':
            if computer_input == 'paper':
                print('Tie!')
            elif computer_input == 'scissors':
                print('Computer wins!')
            elif computer_input == 'rock':
                print('You win!')
        if user_input == 'scissors':
            if computer_input == 'scissors':
                print('Tie!')
            elif computer_input == 'rock':
                print('Computer wins!')
            elif computer_input == 'paper':
                print('You win!')
    else:
        # Invalid input
        game_over = input('Invalid input! You should type in either rock, paper or scissors. Wanna try again(y/n): ').lower()
        if game_over == 'y' or game_over == 'yes':
            game()
        else:
            return

# Call game
game()

