# ile ma mieć znaków
# czy ma mieć liczby
# czy ma mieć duże litery
# czy ma mieć znaki specjalne
# 
#   duze_litery = input("Czy mają być uwzględnione DUŻE litery?: ")
  
#   znaki_specjalne = input("Czy mają być uwzględnione ZNAKI specjalne?: ")
  
#   print("Hasło ma mieć ", liczba_znakow, " znaków.")
import random

#losowe losowanie danej liczby znaków z większego zakresu znaków
liczba = int(input("wstaw liczbę: "))
print(liczba)
test = random.sample(range(0, 9), liczba)
print(test)

#ilość znaków specjalnych 32 ostatni to ]
special_signs = '[`~!@#$%^&*()_-+={[}|\:;"<,>.?/]' 

print(special_signs[31])

print(len(special_signs))

random_number = random.randint(0,31)

wybor = special_signs[random_number]

print(wybor)

# while True:
  
#   liczba_znakow = input("Ile Twoje hasło ma mieć znaków?: ")
#   if liczba_znakow.isdigit():
#     liczba_znakow = int(liczba_znakow)
#   else:
#     print("Następnym razem - wpisz liczbę")
#     continue
  
