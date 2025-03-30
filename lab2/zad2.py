from sklearn import datasets
from sklearn.decomposition import PCA
import pandas as uwu
import matplotlib.pyplot as wykres
import numpy as numpy

iris = datasets.load_iris()
x = uwu.DataFrame(iris.data, columns=iris.feature_names)
y = uwu.Series(iris.target, name='FlowerType')
print(x.head())

pca_iris = PCA(n_components=3).fit(iris.data)
print(pca_iris)
print(pca_iris.explained_variance_ratio_)
print(pca_iris.components_) 
print(pca_iris.transform(iris.data))

skumulowana_wariancja = pca_iris.explained_variance_ratio_.cumsum()
print("skumulowana wariancja", skumulowana_wariancja)

komponenty_n_95 = numpy.argmax(skumulowana_wariancja >= 0.95) + 1
print("komponenty_n_95", komponenty_n_95)
#!!

pca_iris = PCA(n_components=2).fit(iris.data)
xD2 = pca_iris.transform(iris.data)

wykres.figure()
wykres.scatter(xD2[:, 0], xD2[:, 1], c=y, cmap='rainbow', edgecolor='k')
wykres.title("Wizualizacja PCA (2 składowe)")
wykres.xlabel("PC1")
wykres.ylabel("PC2")
wykres.grid(True)
wykres.show()