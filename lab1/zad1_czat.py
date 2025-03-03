import math
import datetime

def calculate_biorhythm(t, cycle):
    return math.sin(2 * math.pi * t / cycle)

def main():
    name = input("Podaj swoje imię: ")
    year = int(input("Podaj rok urodzenia: "))
    month = int(input("Podaj miesiąc urodzenia: "))
    day = int(input("Podaj dzień urodzenia: "))
    
    birth_date = datetime.date(year, month, day)
    today = datetime.date.today()
    days_alive = (today - birth_date).days
    
    physical = calculate_biorhythm(days_alive, 23)
    emotional = calculate_biorhythm(days_alive, 28)
    intellectual = calculate_biorhythm(days_alive, 33)
    
    print(f"\nCześć, {name}! Dziś jest {today}, a ty żyjesz już {days_alive} dni.")
    print(f"Twój biorytm na dziś:")
    print(f"  Fizyczny: {physical:.2f}")
    print(f"  Emocjonalny: {emotional:.2f}")
    print(f"  Intelektualny: {intellectual:.2f}")
    
    def check_status(value, name):
        if value > 0.5:
            print(f"  👍 {name} jest wysoki! To dobry dzień!")
        elif value < -0.5:
            print(f"  😞 {name} jest niski. Może to być trudniejszy dzień.")
        
    check_status(physical, "Fizyczny")
    check_status(emotional, "Emocjonalny")
    check_status(intellectual, "Intelektualny")
    
    # Sprawdzenie, czy następny dzień będzie lepszy
    next_physical = calculate_biorhythm(days_alive + 1, 23)
    next_emotional = calculate_biorhythm(days_alive + 1, 28)
    next_intellectual = calculate_biorhythm(days_alive + 1, 33)
    
    def compare_tomorrow(today_value, tomorrow_value, name):
        if today_value < -0.5:
            if tomorrow_value > today_value:
                print(f"  🌅 {name} jutro się poprawi!")
            else:
                print(f"  🌧 {name} jutro będzie jeszcze gorszy...")
    
    compare_tomorrow(physical, next_physical, "Fizyczny")
    compare_tomorrow(emotional, next_emotional, "Emocjonalny")
    compare_tomorrow(intellectual, next_intellectual, "Intelektualny")
    
if __name__ == "__main__":
    main()
