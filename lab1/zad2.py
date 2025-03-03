import random
import math
import matplotlib.pyplot as plt
import numpy as np

cel = random.randint(50, 340)
print("Cel znajduje się na odległości: ", cel, "m")


v=50
h=100

def oblicz_zasieg(v0, h, alpha):
    g = 9.81
    alpha_rad = math.radians(alpha)
    
    v0x = v0 * math.cos(alpha_rad)
    v0y = v0 * math.sin(alpha_rad)
    
    t = (v0y + math.sqrt(v0y**2 + 2 * g * h)) / g

    x = v0x * t
    
    return x

def rysuj_trajektorie(v0, h, alpha):
    g = 9.81
    alpha_rad = math.radians(alpha)
    
    v0x = v0 * math.cos(alpha_rad)
    v0y = v0 * math.sin(alpha_rad)
    
    t_max = (v0y + math.sqrt(v0y**2 + 2 * g * h)) / g
    
    t_values = np.linspace(0, t_max, num=100)
    x_values = v0x * t_values
    y_values = h + v0y * t_values - 0.5 * g * t_values**2
    
    plt.figure(figsize=(8, 5))
    plt.plot(x_values, y_values, 'b', label='Trajektoria pocisku')
    plt.xlabel("Odległość (m)")
    plt.ylabel("Wysokość (m)")
    plt.title("Trajektoria pocisku naszej świętej inkwizycyjnej katapulty")
    plt.grid()
    plt.savefig("trajektoria.png")
    plt.show()


def znajdz_kat(v0, h, cel):
    g = 9.81
    for kat in range(0, 91):
        zasieg = oblicz_zasieg(v0, h, kat)
        if cel - 5 <= zasieg <= cel + 5:
            return kat
    return None

kat_trafienia = znajdz_kat(v, h, cel)
if kat_trafienia is not None:
    print(f"Aby trafić cel na odległości {cel}m, należy wystrzelić pod kątem {kat_trafienia} stopni.")
else:
    print("Nie znaleziono odpowiedniego kąta do trafienia celu.")

proby = 0
while True:
    kat = input("Podaj kąt strzału: ")
    kat = int(kat)
    if kat not in range(0, 91):
        print("Kąt musi być liczbą z zakresu 0-90 stopni.")
        continue
    zasieg = oblicz_zasieg(v, h, kat)
    if cel - 5 <= zasieg <= cel + 5:
        print("Cel trafiony! Bracia! Bij heretyka kto w Boga wierzy!")
        rysuj_trajektorie(v, h, kat)
        print("Liczba prób: ", proby)
        break
    else:
        print("Pudło! Spróbuj jeszcze raz.")
        proby += 1
        continue

