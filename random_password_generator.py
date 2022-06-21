
# the user chooses the length of a password he wants to get, and the password consisting of digits, capital and small letters and special signs is generated.

import random
import string

#here You choose how long the password is
length = input("How long should the password be?: ")

# here You choose the random digits from 0-9
random_digits = random.sample(range(0, 9), 9)

# here the lowercase letters from the alphabet are chosen
random_lowercase_letters = random.sample(string.ascii_lowercase, 25)

# here the uppercase letters from the alphabet are chosen
random_uppercase_letters = random.sample(string.ascii_uppercase, 25)

# here the special signs eg.#$%@
special_signs = '#%&$()*+,-.:;=?@[]^_{|}~'

# here the special signs are chosen
special_signs = random.sample(special_signs, 23)

# here all elements are added together
wynik = random_digits + random_lowercase_letters + random_uppercase_letters + special_signs

# here all elements are shuffled
random.shuffle(wynik)

# here all commas and brackets are removed
wynik = ''.join(map(str, wynik))

# here is the result
print(wynik[0:int(length)])




