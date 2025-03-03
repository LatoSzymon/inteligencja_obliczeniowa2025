import math
from dateutil import relativedelta
from datetime import date

imie = input("Podaj swoje imię: ")

def sprawdz(imie, rok, miesiac, dzien):
    if (imie == "" or imie.isnumeric() == True):
        print("Podaj poprawne imię")
        return False
    if (rok == "" or rok.isnumeric() == False):
        print("Podaj poprawny rok")
        return False
    if (miesiac == "" or miesiac.isnumeric() == False):
        print("Podaj poprawny miesiąc")
        return False
    if (dzien == "" or dzien.isnumeric() == False):
        print("Podaj poprawny dzień")
        return False


rok = input("Podaj rok urodzenia: ")
miesiac = input("Podaj miesiąc urodzenia: ")
dzien = input("Podaj dzień urodzenia: ")

sprawdz(imie, rok, miesiac, dzien)

data_urodzenia = date(int(rok), int(miesiac), int(dzien))
data_teraz = date.today()
print(data_urodzenia, data_teraz)

delta = data_teraz - data_urodzenia
print(delta)

print("Witamy w Kolonii", imie)
print("Od dnia twego narodzenia minęło tyle dni:", delta.days)

fizyczna_fala = math.sin((2*math.pi*delta.days)/23)
emocjonalna_fala = math.sin((2*math.pi*delta.days)/28)
intelektualna_falalalalalalalalala = math.sin((2*math.pi*delta.days)/33)

print("Twoja fizyczna fala to: ", fizyczna_fala)
print("Zaś twoja emocjonalna wynosi: ", emocjonalna_fala)
print("Natomiast twa fala intelektualna ma postać następującą: ", intelektualna_falalalalalalalalala)

if fizyczna_fala > 0.5:
    print("Fizycznie powinienuś sie czuć git majonez. Zjedz brownie. Albo dwa.")
elif fizyczna_fala < -0.5:
    print("Nie jesteś w formie. Zjedz brownie. Albo dwa.")

if emocjonalna_fala > 0.5:
    print("Emocjonalnie czujesz się chyba cudownie. Zjedz pyszny seruś. Polecam cheddar")
elif emocjonalna_fala < -0.5:
    print("Nie jesteś w formie. Zjedz pyszny seruś. Polecam cheddar")

if intelektualna_falalalalalalalalala > 0.5:
    print("Dziś twoja bystrość jest niedościgniona. Spróbuj zrobić coś trudnego. Może zrób sobie ramen?")
elif intelektualna_falalalalalalalalala < -0.5:
    print("Nie jesteś w formie. Odpuść sobie ciężkie i intelektualne zadania. Może zrób sobie ramen, ale z paczki?")




#zajęło to tak z pół godziny z przerwą na okazjonalne pogaduszki i oglądanie słodkich kotków w sieci


# Pobranie danych od użytkownika
imie = input("Podaj swoje imię: ")

def sprawdz(imie, rok, miesiac, dzien):
    if not imie.isalpha():
        print("Podaj poprawne imię.")
        return False
    if not (rok.isdigit() and miesiac.isdigit() and dzien.isdigit()):
        print("Podaj poprawną datę urodzenia.")
        return False
    return True

rok = input("Podaj rok urodzenia: ")
miesiac = input("Podaj miesiąc urodzenia: ")
dzien = input("Podaj dzień urodzenia: ")

if not sprawdz(imie, rok, miesiac, dzien):
    exit()

# Konwersja na liczby całkowite
rok, miesiac, dzien = int(rok), int(miesiac), int(dzien)

# Obliczenie dni od urodzenia
data_urodzenia = date(rok, miesiac, dzien)
data_teraz = date.today()
delta = (data_teraz - data_urodzenia).days

# Obliczenie wartości biorytmów
fizyczna_fala = math.sin((2 * math.pi * delta) / 23)
emocjonalna_fala = math.sin((2 * math.pi * delta) / 28)
intelektualna_fala = math.sin((2 * math.pi * delta) / 33)

# Obliczenie biorytmów na następny dzień
fizyczna_jutro = math.sin((2 * math.pi * (delta + 1)) / 23)
emocjonalna_jutro = math.sin((2 * math.pi * (delta + 1)) / 28)
intelektualna_jutro = math.sin((2 * math.pi * (delta + 1)) / 33)

# Powitanie
print(f"\nWitamy w Kolonii, {imie}!")
print(f"Od dnia twojego narodzenia minęło {delta} dni.\n")

# Wyświetlenie biorytmów
print(f"Twoja fizyczna fala: {fizyczna_fala:.2f}")
print(f"Twoja emocjonalna fala: {emocjonalna_fala:.2f}")
print(f"Twoja intelektualna fala: {intelektualna_fala:.2f}\n")

# Analiza wyników
def ocena_fali(fala, fala_jutro, opis):
    if fala > 0.5:
        print(f"{opis} poziomie! To świetny dzień! Wykorzystaj go na maxa.")
    elif fala < -0.5:
        print(f"{opis} niskim poziomie. Może być ciężko.")
        if fala_jutro > fala:
            print("Nie martw się. Jutro będzie lepiej!\n")
        else:
            print("Trzymaj się, może być ciężki okres.\n")

ocena_fali(fizyczna_fala, fizyczna_jutro, "Fizycznie jesteś na")
ocena_fali(emocjonalna_fala, emocjonalna_jutro, "Emocjonalnie jesteś na")
ocena_fali(intelektualna_fala, intelektualna_jutro, "Intelektualnie jesteś na")
.
