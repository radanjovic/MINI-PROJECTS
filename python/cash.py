# A program that calculates the minimum number of coins 
# required to give a user change

from cs50 import get_float

# Initializing variables
quarter = 25
dime = 10
nickel = 5
penny = 1

# Initializing counter
n = 0


# Creating function to get input from user
def get_change():
    while True:
        change_owed = get_float("Change owed: ")
        if change_owed > 0:
            break
    return change_owed


# Mapping users input to a var
change = get_change()

# Changing it to cents
cents = change * 100


# Creating loop to go through cents and find the
# number of coins
while cents != 0:
    if cents >= quarter:
        cents = cents - quarter
        n += 1
    elif cents >= dime:
        cents = cents - dime
        n += 1
    elif cents >= nickel:
        cents = cents - nickel
        n += 1
    else:
        cents = cents - penny
        n += 1
print(n)