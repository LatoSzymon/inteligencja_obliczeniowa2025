from matplotlib import pyplot as plt
from matplotlib.image import imread
from os import makedirs, listdir
from os.path import exists
from shutil import copyfile
from random import seed, random

# Folder z oryginalnymi danymi
folder = 'dogs-cats-mini/'

# Tworzenie głównego katalogu datasetu w folderze lab5
dataset_home = 'lab5/dataset_dogs_vs_cats/'
subdirs = ['train/', 'test/']

# Tworzenie podkatalogów dla zbiorów treningowego i testowego
for subdir in subdirs:
    labeldirs = ['pieski/', 'kotki/']
    for labeldir in labeldirs:
        newdir = dataset_home + subdir + labeldir
        makedirs(newdir, exist_ok=True)

# Ustawienie ziarna generatora liczb losowych dla powtarzalności
seed(292572)

# Proporcja danych przeznaczonych na walidację
val_ratio = 0.25

# Kopiowanie obrazów do odpowiednich katalogów
src_directory = 'lab5/dogs-cats-mini/'

# Sprawdzenie, czy katalog źródłowy istnieje
if not exists(src_directory):
    raise FileNotFoundError(f"Katalog {src_directory} nie istnieje. Upewnij się, że ścieżka jest poprawna.")

# Sprawdzenie zawartości katalogu źródłowego
print("Pliki w katalogu źródłowym:", listdir(src_directory))

for file in listdir(src_directory):
    src = src_directory + '/' + file
    dst_dir = 'train/'
    # Losowe przypisanie do zbioru testowego na podstawie val_ratio
    if random() < val_ratio:
        dst_dir = 'test/'
    # Przypisanie plików do odpowiednich folderów na podstawie nazwy
    if file.startswith('cat'):
        dst = dataset_home + dst_dir + 'kotki/' + file
        print(f"Kopiowanie pliku {src} do {dst}")
        copyfile(src, dst)
    elif file.startswith('dog'):
        dst = dataset_home + dst_dir + 'pieski/' + file
        print(f"Kopiowanie pliku {src} do {dst}")
        copyfile(src, dst)
