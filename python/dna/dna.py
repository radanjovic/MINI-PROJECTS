# A program that indentifies a person based on their DNA

# DNA, the carrier of genetic information in living things, has been used in criminal 
# justice for decades. But how, exactly, does DNA profiling work? Given a sequence of 
# DNA, how can forensic investigators identify to whom it belongs?

# Well, DNA is really just a sequence of molecules called nucleotides, arranged into a 
# particular shape (a double helix). Each nucleotide of DNA contains one of four different 
# bases: adenine (A), cytosine (C), guanine (G), or thymine (T). Every human cell has 
# billions of these nucleotides arranged in sequence. Some portions of this sequence 
# (i.e. genome) are the same, or at least very similar, across almost all humans, but 
# other portions of the sequence have a higher genetic diversity and thus vary more across
#  the population.

# One place where DNA tends to have high genetic diversity is in Short Tandem Repeats 
# (STRs). An STR is a short sequence of DNA bases that tends to repeat consecutively 
# numerous times at specific locations inside of a person’s DNA. The number of times 
# any particular STR repeats varies a lot among individuals. In the DNA samples below,
#  for example, Alice has the STR AGAT repeated four times in her DNA, while Bob has 
#  the same STR repeated five times.

# Using multiple STRs, rather than just one, can improve the accuracy of DNA profiling.
#  If the probability that two people have the same number of repeats for a single STR 
#  is 5%, and the analyst looks at 10 different STRs, then the probability that two DNA
#   samples match purely by chance is about 1 in 1 quadrillion (assuming all STRs are 
#   independent of each other). So if two DNA samples match in the number of repeats for
#    each of the STRs, the analyst can be pretty confident they came from the same person.
#     CODIS, The FBI’s DNA database, uses 20 different STRs as part of its DNA profiling 
#     process.

# What might such a DNA database look like? Well, in its simplest form, you could imagine
#  formatting a DNA database as a CSV file, wherein each row corresponds to an individual,
#   and each column corresponds to a particular STR.

# name,AGAT,AATG,TATC
# Alice,28,42,14
# Bob,17,22,19
# Charlie,36,18,25

# The data in the above file would suggest that Alice has the sequence AGAT repeated 28
#  times consecutively somewhere in her DNA, the sequence AATG repeated 42 times, and TATC
#   repeated 14 times. Bob, meanwhile, has those same three STRs repeated 17 times, 22
#    times, and 19 times, respectively. And Charlie has those same three STRs repeated 36,
#     18, and 25 times, respectively.

# So given a sequence of DNA, how might you identify to whom it belongs? Well, imagine that
#  you looked through the DNA sequence for the longest consecutive sequence of repeated 
#  AGATs and found that the longest sequence was 17 repeats long. If you then found that 
#  the longest sequence of AATG is 22 repeats long, and the longest sequence of TATC is 19
#   repeats long, that would provide pretty good evidence that the DNA was Bob’s. Of course,
#    it’s also possible that once you take the counts for each of the STRs, it doesn’t match
#     anyone in your DNA database, in which case you have no match.

# In practice, since analysts know on which chromosome and at which location in the DNA an
#  STR will be found, they can localize their search to just a narrow section of DNA. But
#   we’ll ignore that detail for this problem.

import csv
import sys


def main():

    # Making sure we have the right amount of cmd line args
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py name_of_CSV_file name_of_text_file")

    # Storing provided args into variable in order to open
    # them later on.
    csv_file = sys.argv[1]
    text_file = sys.argv[2]

    # Creating list of databases and count dict which we'll
    # populate later
    database = []
    count = {}

    # Opening csv files and populating our list of databases
    # with dictionaries.
    with open(csv_file, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            database.append(row)

    # Instead of manually populating count, which creates problem
    # later on with the small.csv, we'll, with the help of this
    # simple loop, pass the keys from database to our count dict
    # without the 'name' key and value, ofc.
    for i in range(len(database)):
        for j in database[i]:
            if j == 'name':
                continue
            count[j] = 0

    # Opening our text file and reading the contents into
    # a string called sequence, and then, calling on a
    # function we wrote called count strs to count the strs
    # and populate our count dictionary, through a loop.
    with open(text_file, "r") as file2:
        sequence = file2.read()
        for key in count:
            count[key] = count_strs(sequence, key)

    # Finally, checking if a specific sequence is in database
    # We do this via loops, in which we check if a value from
    # specific key is the in both count and database, and if is
    # we then increment our match counter by one. If at the end
    # our match counter is equall to lenght of our count, which
    # would mean that all the values match, we have our match
    # and we just print the name, after which we exit with a 0.
    # If no match is found - we print No match and exit.
    for i in range(len(database)):
        if database[i] == 'name':
            continue
        for j in database[i]:
            match = 0
            for k in count:
                if int(database[i][k]) == count[k]:
                    match += 1
            if match == len(count):
                print(database[i]['name'])
                sys.exit(0)

    print("No match")
    sys.exit(0)


# Creating a separate function to find the longest strs in
# succession, so that we can use loop in main for each of
# the keys. This function was helped by others from the
# web.
def count_strs(sequence, key):
    l = len(key)
    longest = 0

    for i in range(len(sequence)):
        counter = 0

        if sequence[i:i+l] == key:
            counter += 1

            while sequence[i:i+l] == sequence[i+l:i+(2*l)]:
                counter += 1
                i += l

        if counter > longest:
            longest = counter
    return longest


# Calling main.
main()