import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.datasets import load_iris 
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler, OneHotEncoder 
from tensorflow.keras.models import Sequential 
from tensorflow.keras.layers import Dense 
from tensorflow.keras.utils import plot_model 
 
# Load the iris dataset 
iris = load_iris() 
X = iris.data 
y = iris.target 
 
# Preprocess the data 
# Scale the features 
scaler = StandardScaler() 
X_scaled = scaler.fit_transform(X) 
 
# Encode the labels 
encoder = OneHotEncoder(sparse_output=False) 
y_encoded = encoder.fit_transform(y.reshape(-1, 1)) 
 
# Split the dataset into training and test sets 
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_encoded, test_size=0.3, 
random_state=292572) 
 
# Define the model with tanh activation
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    Dense(64, activation='relu'),  # Zmiana z relu na elu
    Dense(y_encoded.shape[1], activation='softmax')  # Warstwa wyjściowa pozostaje bez zmian
])

# Compile the model
model.compile(optimizer='adam', loss='mse', metrics=['accuracy'])

# Train the model
history = model.fit(X_train, y_train, epochs=100, validation_split=0.2)

# Evaluate the model on the test set
test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"Test Accuracy: {test_accuracy*100:.2f}%")
 
# Plot the learning curve 
plt.figure(figsize=(12, 6)) 
plt.subplot(1, 2, 1) 
plt.plot(history.history['accuracy'], label='train accuracy') 
plt.plot(history.history['val_accuracy'], label='validation accuracy') 
plt.title('Model accuracy') 
plt.ylabel('Accuracy') 
plt.xlabel('Epoch') 
plt.grid(True, linestyle='--', color='grey') 
plt.legend() 
 
plt.subplot(1, 2, 2) 
plt.plot(history.history['loss'], label='train loss') 
plt.plot(history.history['val_loss'], label='validation loss') 
plt.title('Model loss') 
plt.ylabel('Loss') 
plt.xlabel('Epoch') 
plt.grid(True, linestyle='--', color='grey') 
plt.legend() 
 
plt.tight_layout() 
plt.show() 
 
# Save the model 
model.save('iris_model.h5') 
 
# Plot and save the model architecture 
plot_model(model, to_file='model_plot.png', show_shapes=True, show_layer_names=True)

"""
a) StandardScaler to narzędzie do standaryzacji danych poprzez przekształcenie ich tak,
 żeby miały średnią 0 i odchylenie standardowe 1.

b) OneHotEncoder to narzędzie do kodowania etykiet kategorii jako wektory binarne. Kodowanie one-hot jest
techniką reprezentacji danych, w której każda kategoria jest reprezentowana jako wektor binarny

c) warstwa wejściowa: 4, bo dla każdej cechy
obie ukryte warstwy mają po 64
wyjściowa: 3, bo dla 3 gatunków

d) relu - 95,56%
 tanh - 97,78%
 elu - 97,78% 
 co ciekawe, wychodzi na to że relu nie jest najlepszym wyborem, a elu daje takie same wyniki jak tanh

e) adam - 95,56%
sgd - 82,22%
adagrad - 77,78%
więc adam jest lepszy

co do funkcji straty:
categorical_crossentropy - 97,78%
mse - 93,33%

Większa szybkość uczenia się: Model szybciej się uczy, ale może nie osiągnąć optymalnego minimum.
Mniejsza szybkość uczenia się: Model uczy się wolniej, ale może osiągnąć lepsze wyniki.

f)
im wiekszy rozmiar partii, tym krzywe uczenia są bardziej gładkie,
ale mogą potrzebować więcej epok zeby dostarczyć optymalne wyniki.

g)
mamy tu do czynienia raczej z dobrym dopasowaniem, bo nie ma dużej różnicy między treningiem a walidacją
model zaś osiągnął najlepszą wydajność w okolicach epoki 50-60, bo tam dokładno
"""
