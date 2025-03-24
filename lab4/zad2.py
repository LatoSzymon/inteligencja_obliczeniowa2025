from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=292572
)

print("Rozmiar zbioru treningowego:", X_train.shape)
print("Rozmiar zbioru testowego:", X_test.shape)

print("Przykładowe etykiety (numery gatunków) w zbiorze treningowym:", y_train[:5])
print("Odpowiadają one gatunkom:")
for idx, gatunek in enumerate(iris.target_names):
    print(f"{idx} -> {gatunek}")
    
mlp_2 = MLPClassifier(hidden_layer_sizes=(2,), max_iter=2000, random_state=42)
mlp_2.fit(X_train, y_train)
pred_2 = mlp_2.predict(X_test)
acc_2 = accuracy_score(y_test, pred_2)
print("[Architektura (2)] Dokładność:", acc_2)

mlp_3 = MLPClassifier(hidden_layer_sizes=(3,), max_iter=2000, random_state=42)
mlp_3.fit(X_train, y_train)
pred_3 = mlp_3.predict(X_test)
acc_3 = accuracy_score(y_test, pred_3)
print("[Architektura (3)] Dokładność:", acc_3)

mlp_3x2 = MLPClassifier(hidden_layer_sizes=(3, 3), max_iter=2000, random_state=42)
mlp_3x2.fit(X_train, y_train)
pred_3x2 = mlp_3x2.predict(X_test)
acc_3x2 = accuracy_score(y_test, pred_3x2)
print("[Architektura (3,3)] Dokładność:", acc_3x2)

print("Porównywanie dokładności, bo jest różna jak rybie ości:")
print("Sieć (2):   ", acc_2)
print("Sieć (3):   ", acc_3)
print("Sieć (3,3): ", acc_3x2)
