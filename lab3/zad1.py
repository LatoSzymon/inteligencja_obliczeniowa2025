import pandas as miau
from sklearn.model_selection import train_test_split

df = miau.read_csv("c:/Users/szymo/repozytoria/int2025/inteligencja_obliczeniowa2025/lab3/iris1 (1).csv")

(treningowanie, testowanie) = train_test_split(df.values, test_size=0.7, random_state=292572)

treningowanie_ale_posortowane = treningowanie[treningowanie[:, 4].argsort()]

print("tutututut tequila tutututu")
def zklasyfikuj_se_irysa(spel, swel, pel, pwel):
    if pel > 1 and pel <2:
        return "Setosa"
    elif pel > 3.5 and pel < 5:
        return "Versicolor"
    else:
        return "Virginica"
    
dobre_zgadywanki = 0
bawelna = treningowanie.shape[0]

for i in range(bawelna):
    if zklasyfikuj_se_irysa(treningowanie[i][0], treningowanie[i][1], treningowanie[i][2], treningowanie[i][3]) == treningowanie[i][4]:
        dobre_zgadywanki += 1

print("Dokładność klasyfikacji:", dobre_zgadywanki / bawelna*100, "%")

#odpowiedź: 35,(5)%, to nawet nie tyle co wódka