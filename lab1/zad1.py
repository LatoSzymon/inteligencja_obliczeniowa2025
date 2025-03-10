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
    print("Nie jesteś w formie fizycznej dziś. Zjedz brownie. Albo dwa.")

if emocjonalna_fala > 0.5:
    print("Emocjonalnie czujesz się chyba cudownie. Zjedz pyszny seruś. Polecam cheddar")
elif emocjonalna_fala < -0.5:
    print("Nie jesteś w formie. Zjedz pyszny seruś. Polecam cheddar")

if intelektualna_falalalalalalalalala > 0.5:
    print("Dziś twoja bystrość jest niedościgniona. Spróbuj zrobić coś trudnego. Może zrób sobie ramen?")
elif intelektualna_falalalalalalalalala < -0.5:
    print("Nie jesteś w formie. Odpuść sobie ciężkie i intelektualne zadania. Może zrób sobie ramen, ale z paczki?")




#zajęło to tak z pół godziny z przerwą na okazjonalne pogaduszki i oglądanie słodkich kotków w sieci


