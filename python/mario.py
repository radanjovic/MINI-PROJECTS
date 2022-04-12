# A program that prints out a double half-pyramid of a specified height
# just like in Mario game

from cs50 import get_int

# Creating a do-while loop in python


def do_while():
    while True:
        n = get_int("Height: ")
        if n > 0 and n < 9:
            break
    return n


n = do_while()

# Creating main loop - which is in python also the only one.
# Inside it, by manipulating only print function, we can
# achive the same we did in C (for which we needed additional
# loops).

for i in range(n):
    print(" " * (n - i - 1), end="")
    print("#" * (i + 1), end="")
    print("  ", end="")
    print("#" * (i + 1))