#different random operations
import random

#losowe losowanie danej liczby znaków z większego zakresu znaków
number_of_numbers = int(input("insert number of numbers to be selected: "))
print(number_of_numbers)
test = random.sample(range(0, 100), number_of_numbers)
print(test)