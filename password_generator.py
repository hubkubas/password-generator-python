# ile ma mieć znaków
# czy ma mieć liczby
# czy ma mieć duże litery
# czy ma mieć znaki specjalne
import random

special = '[(_:/,#%\=@$)]'

random_numer = random.randint(0,11)

wybor = special[random_numer]

print(wybor)

# while True:
  
#   liczba_znakow = input("Ile Twoje hasło ma mieć znaków?: ")
#   if liczba_znakow.isdigit():
#     liczba_znakow = int(liczba_znakow)
#   else:
#     print("Następnym razem - wpisz liczbę")
#     continue
  
#   duze_litery = input("Czy mają być uwzględnione DUŻE litery?: ")
  
#   znaki_specjalne = input("Czy mają być uwzględnione ZNAKI specjalne?: ")
  
#   print("Hasło ma mieć ", liczba_znakow, " znaków.")