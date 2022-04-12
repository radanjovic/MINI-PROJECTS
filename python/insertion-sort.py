# Implementing insertion sorting algorithm
import time
import random

def insertionSort(l):
    i = 1
    # Main loop
    while i < len(l):
        current = l[i]
        j = i - 1
        # Sub loop
        while j >= 0 and l[j] > current:
            l[j+1] = l[j]
            j = j - 1
        l[j+1] = current
        i = i + 1
    return l

# Generating random list of 1000 numbers in range from 1 to 1M
list1 = random.sample(range(1, 1000000), 1000)

# Getting time too
start = time.time()
sorted = insertionSort(list1)
end = time.time()

# Printing results
print(sorted)
print("Time: --- {} --- seconds".format(end - start))