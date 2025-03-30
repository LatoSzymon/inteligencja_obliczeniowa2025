from sklearn import datasets
from sklearn.model_selection import train_test_split
import pandas as uwu
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

irysy = datasets.load_iris()
print(irysy.values)
x = uwu.DataFrame(irysy.data, columns=irysy.feature_names)
y = uwu.Series(irysy.target, name='FlowerType')

trenujemy_x, test_x, trenujemy_y, test_y = train_test_split(x, y, test_size=0.3, random_state=292572)

print("ZBIÓR TRENINGOWY X:")
print(trenujemy_x.head())

print("ZBIÓR TRENINGOWY Y:")
print(trenujemy_y.head())

print("ZBIÓR TESTOWY X:")
print(test_x.head())

print("ZBIÓR TESTOWY Y:")
print(test_y.head())

Drzewko = DecisionTreeClassifier()
Drzewko.fit(trenujemy_x, trenujemy_y)

plt.figure(figsize=(20,10))
plot_tree(Drzewko, feature_names=irysy.feature_names, class_names=irysy.target_names, filled=True, proportion=True, rounded=True, fontsize=12)
plt.show()

dokladnosc = Drzewko.score(test_x, test_y)
print("Dokładność klasyfikatora jest następująca: ", dokladnosc)

macierz_konfuzji = confusion_matrix(test_y, Drzewko.predict(test_x))
print("Macierz konfuzji:")
print(macierz_konfuzji)

plt.figure(figsize=(10,7))
sns.heatmap(macierz_konfuzji, annot=True, cmap='Blues', fmt='g')

plt.xlabel('Predicted labels')
plt.ylabel('True labels')
plt.title('Confusion Matrix')
plt.show()