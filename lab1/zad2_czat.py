import numpy as np
import matplotlib.pyplot as plt
import random

g = 9.81  # przyspieszenie ziemskie [m/s^2]
v0 = 50   # prędkość początkowa [m/s]
h = 100   # wysokość trebusza [m]

# Funkcja obliczająca zasięg rzutu ukośnego z wysokości
def calculate_range(angle):
    angle_rad = np.radians(angle)
    term1 = v0 * np.cos(angle_rad) / g
    term2 = v0 * np.sin(angle_rad) + np.sqrt((v0 * np.sin(angle_rad))**2 + 2 * g * h)
    return term1 * term2

# Losowanie odległości celu
target = random.randint(50, 340)
print(f"Cel znajduje się w odległości: {target} m")

attempts = 0

while True:
    try:
        angle = float(input("Podaj kąt strzału w stopniach: "))
        distance = calculate_range(angle)
        print(f"Pocisk przeleciał {distance:.2f} metrów.")
        attempts += 1

        if target - 5 <= distance <= target + 5:
            print(f"Cel trafiony! Liczba prób: {attempts}")
            break
        else:
            print("Chybiony! Spróbuj ponownie.")
    except ValueError:
        print("Niepoprawna wartość. Wprowadź liczbę.")

# Rysowanie trajektorii trafionego strzału
def plot_trajectory(angle):
    angle_rad = np.radians(angle)
    t_flight = (v0 * np.sin(angle_rad) + np.sqrt((v0 * np.sin(angle_rad))**2 + 2 * g * h)) / g
    t = np.linspace(0, t_flight, num=500)
    x = v0 * np.cos(angle_rad) * t
    y = h + v0 * np.sin(angle_rad) * t - 0.5 * g * t**2

    plt.figure(figsize=(10, 5))
    plt.plot(x, y, label="Trajektoria pocisku", color='blue')
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(target, color='red', linestyle='--', label="Cel")
    plt.xlabel("Odległość [m]")
    plt.ylabel("Wysokość [m]")
    plt.title("Trajektoria pocisku Warwolf")
    plt.legend()
    plt.grid()
    plt.savefig("trajektoria.png")
    plt.show()

plot_trajectory(angle)
