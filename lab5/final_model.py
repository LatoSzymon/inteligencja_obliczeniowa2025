# Importy
import sys
from matplotlib import pyplot
from keras.applications.vgg16 import VGG16
from keras.models import Model
from keras.layers import Dense, Flatten
from keras.optimizers import SGD
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Definicja modelu CNN z transfer learningiem
def define_model():
    # Wczytanie modelu VGG16 bez warstw wierzchnich
    model = VGG16(include_top=False, input_shape=(224, 224, 3))
    # Zamrożenie wag w wczytanych warstwach
    for layer in model.layers:
        layer.trainable = False
    # Dodanie nowych warstw klasyfikatora
    flat1 = Flatten()(model.layers[-1].output)
    class1 = Dense(128, activation='relu', kernel_initializer='he_uniform')(flat1)
    output = Dense(1, activation='sigmoid')(class1)
    # Zdefiniowanie nowego modelu
    model = Model(inputs=model.inputs, outputs=output)
    # Kompilacja modelu
    opt = SGD(learning_rate=0.001, momentum=0.9)
    model.compile(optimizer=opt, loss='binary_crossentropy', metrics=['accuracy'])
    return model

# Wizualizacja krzywych uczenia
def summarize_diagnostics(history):
    # Wykres strat
    pyplot.subplot(211)
    pyplot.title('Cross Entropy Loss')
    pyplot.plot(history.history['loss'], color='blue', label='train')
    pyplot.plot(history.history['val_loss'], color='orange', label='test')
    # Wykres dokładności
    pyplot.subplot(212)
    pyplot.title('Classification Accuracy')
    pyplot.plot(history.history['accuracy'], color='blue', label='train')
    pyplot.plot(history.history['val_accuracy'], color='orange', label='test')
    # Zapis wykresów do pliku
    filename = sys.argv[0].split('/')[-1]
    pyplot.savefig(filename + '_plot.png')
    pyplot.close()

# Uruchomienie procesu trenowania i ewaluacji modelu
def run_test_harness():
    # Definicja modelu
    model = define_model()
    # Przygotowanie generatora danych
    datagen = ImageDataGenerator(featurewise_center=True)
    # Średnie wartości z ImageNet do centrowania
    datagen.mean = [123.68, 116.779, 103.939]
    # Przygotowanie iteratorów danych
    train_it = datagen.flow_from_directory('lab5/dataset_dogs_vs_cats/train/',
        class_mode='binary', batch_size=64, target_size=(224, 224))
    test_it = datagen.flow_from_directory('lab5/dataset_dogs_vs_cats/test/',
        class_mode='binary', batch_size=64, target_size=(224, 224))
    # Trenowanie modelu
    history = model.fit(train_it, steps_per_epoch=len(train_it),
        validation_data=test_it, validation_steps=len(test_it), epochs=10, verbose=1)
    # Ewaluacja modelu
    _, acc = model.evaluate(test_it, steps=len(test_it), verbose=0)
    print('> %.3f' % (acc * 100.0))
    # Wizualizacja krzywych uczenia
    summarize_diagnostics(history)
    # Zapisanie modelu do pliku
    model.save('final_model.h5')

# Punkt wejścia
run_test_harness()