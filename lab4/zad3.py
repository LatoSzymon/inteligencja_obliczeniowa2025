import pandas as uwu
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix


pączuszki = uwu.read_csv(r"C:\Users\Szymon\repo\inteligencja_obliczeniowa2025\lab4\diabetes_1.csv")

pączuszki['class'] = pączuszki['class'].map({'tested_positive': 1, 'tested_negative': 0})

train, test = train_test_split(pączuszki, test_size=0.3, random_state=292572)

x_train = train.drop('class', axis=1)
y_train = train['class']
x_test = test.drop('class', axis=1)
y_test = test['class']

mlep = MLPClassifier(hidden_layer_sizes=(6,3), activation='relu', max_iter=500, random_state=292572)

mlep.fit(x_train, y_train)

y_pred = mlep.predict(x_test)

dokladnosc = accuracy_score(y_test, y_pred)
print("Dokładność:", dokladnosc)

macierzynstwo = confusion_matrix(y_test, y_pred)
print("Macierz pomyłek:")
print(macierzynstwo)

mlep2 = MLPClassifier(hidden_layer_sizes=(4,2), activation='tanh', max_iter=500, random_state=292572)

mlep2.fit(x_train, y_train)

y_pred2 = mlep2.predict(x_test)

dokladnosc2 = accuracy_score(y_test, y_pred2)
print("Dokładność (mlep2):", dokladnosc2)

macierzynstwo2 = confusion_matrix(y_test, y_pred2)
print("Macierz pomyłek (mlep2):")
print(macierzynstwo2)


#W przypadku cukrzyków (jak np. Scott Malkinson) FN jest gorszy, bo osoba z cukrzyca mogła być zdiagnozowana jako zdrowa
#mlep - więcej FP
#mlep2 - więcej FN









