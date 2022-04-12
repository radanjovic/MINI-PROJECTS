# FizzBuzz challenge - create list of numbers, where if the number is
# divisible with 3, instead of that number put Fizz in list, if number
# is divisible with 5, put Buzz instead, and finally, if number is 
# divisible with both 3 and 5, put FizzBuzz in the list

import time
l = []

# The most effective way to do it
def fizzBuzz():
    for i in range(1, 1001):
        if i % 5 == 0:
            if i % 3 != 0:
                l.append("Buzz")
            else:
                l.append("FizzBuzz")
        elif i % 3 == 0:
            l.append("Fizz")
        else:
            l.append(i)

# Other ways:
# def no1():
#     for i in range(1, 1001):
#         if i % 5 == 0:
#             if i % 3 == 0:
#                 l.append("FizzBuzz")
#             else:
#                 l.append("Buzz")
#         elif i % 3 == 0:
#             l.append("Fizz")
#         else:
#             l.append(i)

# def no2():
#     for i in range(1, 1001):
#         if i % 3 == 0 and i % 5 == 0:
#             l.append("FizzBuzz")
#         elif i % 3 == 0:
#             l.append("Fizz")
#         elif i % 5 == 0:
#             l.append("Buzz")
#         else:
#             l.append(i)

# def no3():
#     for i in range(1, 1001):
#         if i % 3 == 0:
#             if i % 5 == 0:
#                 l.append("FizzBuzz")
#             else:
#                 l.append("Fizz")
#         elif i % 5 == 0:
#             l.append("Buzz")
#         else:
#             l.append(i) 

start = time.time()
fizzBuzz()
end = time.time()
print(l)
print ('Time: --- {} --- seconds'.format(end-start))
