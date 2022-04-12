# Implementing bubble sorting algorithm
import time
import random

def bubbleSort(l):
    # Main loop
    for i in range(len(l)):
        # Nested loop
        for j in range(len(l) -1 - i):
            if l[j] > l[j+1]:
                # Swap
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp
    return l

# Generating random list of 1000 numbers in range from 1 to 1M
list1 = random.sample(range(1, 1000000), 1000)

# Getting time too
start = time.time()
sorted = bubbleSort(list1)
end = time.time()

# Printing results
print(sorted)
print("Time: --- {} --- seconds".format(end - start))