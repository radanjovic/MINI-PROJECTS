# Guess the number game - with random clues that user gets during execution
import random

# Init vars
number_of_tries = 5
random_number = random.randint(1,100)
game_over = False

# Init clues
clues = []

# Get some clues
for i in [10,5,3]:
    if random_number % i == 0:
        clues.append('Number IS divisible by {}'.format(i))
    else:
        clues.append('Number is NOT divisible by {}'.format(i))

# Odd or even
if random_number % 2 == 0:
    clues.append('Number is EVEN')
else:
    clues.append('Number is ODD')

while number_of_tries > 0:
    try:
        if number_of_tries == 1:
            user_input = int(input('Guess a number (1-100). This is your last try: '))
        else:
            user_input = int(input('Guess a number (1-100). You have {} tries left: '.format(number_of_tries)))

        if user_input > 100 or user_input < 1:
            print('Invalid input - Try again by typing in a NUMBER between 1-100')
            break
        if user_input == random_number:
            print('CONGRATULATIONS! YOU GUESSED RIGHT!!!')
            game_over = True
            break
        else:
            random_clue = random.choice(clues)
            clues.remove(random_clue)

            if user_input > random_number:
                print("Your guess is too high! Here's one random clue, on us: {}".format(random_clue))
            else:
                print("Your guess is too low! Here's one random clue, on us: {}".format(random_clue))


        number_of_tries = number_of_tries -1
    except:
        print('Invalid input - Try again by typing in a NUMBER between 1-100')
        break

if game_over == False:
    print('You lost! The number was: {}'.format(random_number))