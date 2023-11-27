"""This file contains examples on how to try/except, cast numbers, and take in user inputs
    also how to take in a string and break it up into pieces"""

try:
    num = int(input("Enter a number: "))
    num += 5
    print(num)
except:
    print("Please enter a number!!!")

with open("movies.txt") as file:
    for line in file:
        print(line.strip())
        print(line)

with open("heights.txt") as file:
    for line in file:
        stripped_line = line.strip()
        tokens = stripped_line.split()
        #print(tokens)
        print(tokens[0], tokens[1], "is", int(tokens[2]), "inches")