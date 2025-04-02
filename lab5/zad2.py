import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
from tensorflow.keras.datasets import mnist 
from tensorflow.keras.models import Sequential 
from tensorflow.keras.layers import Dense, Conv2D, Flatten, MaxPooling2D 
from tensorflow.keras.utils import to_categorical 
from tensorflow.keras.callbacks import History, ModelCheckpoint
  
from sklearn.metrics import confusion_matrix 
 
# Load dataset 
(train_images, train_labels), (test_images, test_labels) = mnist.load_data() 
 
# Preprocess data 
train_images = train_images.reshape((train_images.shape[0], 28, 28, 1)).astype('float32') / 255 
test_images = test_images.reshape((test_images.shape[0], 28, 28, 1)).astype('float32') / 255 
train_labels = to_categorical(train_labels) 
test_labels = to_categorical(test_labels) 
original_test_labels = np.argmax(test_labels, axis=1)
 
# Define model 
model = Sequential([ 
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)), 
    MaxPooling2D((2, 2)), 
    Flatten(), 
    Dense(64, activation='relu'), 
    Dense(10, activation='softmax') 
]) 
 
# Compile model 
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy']) 
 
# Callback to save the model when validation accuracy improves
checkpoint = ModelCheckpoint(
    filepath='best_model.h5',  # Nazwa pliku, w którym zapisany zostanie model
    monitor='val_accuracy',   # Monitorujemy dokładność walidacyjną
    save_best_only=True,      # Zapisujemy tylko, gdy wynik się poprawi
    mode='max',               # Szukamy maksymalnej wartości (dla dokładności)
    verbose=1                 # Wyświetlamy informacje o zapisie modelu
)

# Train model 
history = History() 
history = model.fit(
    train_images, train_labels,
    epochs=5,
    batch_size=64,
    validation_split=0.2,
    callbacks=[history, checkpoint]  # Dodajemy callback do listy
)
 
# Evaluate on test set 
test_loss, test_acc = model.evaluate(test_images, test_labels) 
print(f"Test accuracy: {test_acc:.4f}") 
 
# Predict on test images 
predictions = model.predict(test_images) 
predicted_labels = np.argmax(predictions, axis=1) 
 
# Confusion matrix 
cm = confusion_matrix(original_test_labels, predicted_labels) 
plt.figure(figsize=(10, 7)) 
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues') 
plt.xlabel('Predicted') 
plt.ylabel('True') 
plt.title('Confusion Matrix') 
plt.show() 
 
# Plotting training and validation accuracy 
plt.figure(figsize=(10, 5)) 
plt.subplot(1, 2, 1) 

plt.plot(history.history['accuracy'], label='Training Accuracy') 
plt.plot(history.history['val_accuracy'], label='Validation Accuracy') 
plt.xlabel('Epoch') 
plt.ylabel('Accuracy') 
plt.grid(True, linestyle='--', color='grey') 
plt.legend() 
 
# Plotting training and validation loss 
plt.subplot(1, 2, 2) 
plt.plot(history.history['loss'], label='Training Loss') 
plt.plot(history.history['val_loss'], label='Validation Loss') 
plt.xlabel('Epoch') 
plt.ylabel('Loss') 
plt.grid(True, linestyle='--', color='grey') 
plt.legend() 
 
plt.tight_layout() 
plt.show() 
 
# Display 25 images from the test set with their predicted labels 
plt.figure(figsize=(10,10)) 
for i in range(25): 
    plt.subplot(5,5,i+1) 
    plt.xticks([]) 
    plt.yticks([]) 
    plt.grid(False) 
    plt.imshow(test_images[i].reshape(28,28), cmap=plt.cm.binary) 
    plt.xlabel(predicted_labels[i]) 
plt.show()


"""
a) reshape zmienia kształt danych, aby były zgodne z wymaganiami modelu
    to_categorical zamienia etykiety na wektory one-hot
    np.argmax zamienia wektory one-hot na etykiety
b) Wejście: Obraz (28, 28, 1) → Normalizacja do zakresu [0, 1].
Warstwa konwolucyjna: Wyodrębnia cechy → Tensor (26, 26, 32).
Pooling: Redukuje wymiary → Tensor (13, 13, 32).
Spłaszczenie: Przekształca tensor w wektor → Wektor 5408.
Warstwa ukryta: Przetwarza dane → Wektor 64.
Warstwa wyjściowa: Generuje prawdopodobieństwa klas → Wektor 10.

c) najczęściej mylone jest 5 z 9 i 7 z 1
d) jeśli już to mamy tu lekkie przetrenowanie
e) done
"""