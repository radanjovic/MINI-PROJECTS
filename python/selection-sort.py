# Implementing selection sorting algorithm
import time
import random

def selectionSort(l):
    # Main loop
    for i in range(len(l)-1):
        lower = i
        j = i + 1
        # Nested loop
        while j < len(l):
            if l[lower] > l[j]:
                lower = j
            j = j + 1
        # Swap
        temp = l[i]
        l[i] = l[lower]
        l[lower] = temp
    return l

# Generating random list of 1000 numbers in range from 1 to 1M
list1 = random.sample(range(1, 1000000), 1000)

# Getting time too
start = time.time()
sorted = selectionSort(list1)
end = time.time()

# Printing results
print(sorted)
print("Time: --- {} --- seconds".format(end - start))