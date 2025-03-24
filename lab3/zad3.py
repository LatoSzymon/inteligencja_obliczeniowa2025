from sklearn import datasets
from sklearn.model_selection import train_test_split
import pandas as uwu
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score
import seaborn as sea
import matplotlib.pyplot as plt

irysy = datasets.load_iris()
x = uwu.DataFrame(irysy.data, columns=irysy.feature_names)
y = uwu.Series(irysy.target, name='FlowerType')

trening_x, test_x, trening_y, test_y = train_test_split(x, y, test_size=0.3, random_state=292572)

def droga_dziobaka(classifier, trening_x, trening_y, test_x, test_y, imie_klasyfikatora):
    classifier.fit(trening_x, trening_y)
    przepowiednia_y = classifier.predict(test_x)
    dokladnosc = accuracy_score(test_y, przepowiednia_y)
    macierz_konfuzji = confusion_matrix(test_y, przepowiednia_y)
    
    print("Dokładność klasyfikatora: ", dokladnosc)
    print("Macierz konfuzji:")
    print(macierz_konfuzji)

    plt.figure(figsize=(10,7))
    sea.heatmap(macierz_konfuzji, annot=True, cmap='Blues', fmt='d', xticklabels=irysy.target_names, yticklabels=irysy.target_names)
    plt.xlabel('Predykcja i przewidywanie')
    plt.ylabel('Prawdziwa klasa')
    plt.title('Macierz konfuzji i błędów wszelakich')
    plt.show()

knn3 = KNeighborsClassifier(n_neighbors=3)
droga_dziobaka(knn3, trening_x, trening_y, test_x, test_y, "KNN3")
    
knn5 = KNeighborsClassifier(n_neighbors=5)
droga_dziobaka(knn5, trening_x, trening_y, test_x, test_y, "KNN5")
    
knn11 = KNeighborsClassifier(n_neighbors=11)
droga_dziobaka(knn11, trening_x, trening_y, test_x, test_y, "KNN11")
    
nb = GaussianNB()
droga_dziobaka(nb, trening_x, trening_y, test_x, test_y, "Naive Bayes")
    
classifiers = {
    'k-NN (k=3)': knn3,
    'k-NN (k=5)': knn5,
    'k-NN (k=11)': knn11,
    'Naive Bayes': nb
}
    
accuracies = {}
for name, clf in classifiers.items():
    clf.fit(trening_x, trening_y)
    y_pred = clf.predict(test_x)
    accuracies[name] = accuracy_score(test_y, y_pred)
    
print("Porównanie dokładności klasyfikatorów:")
for name, accuracy in accuracies.items():
    print(f'{name}: {accuracy * 100:.2f}%')
    