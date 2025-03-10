from sklearn import datasets
from sklearn.decomposition import PCA
import pandas as uwu

iris = datasets.load_iris()
x = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target, name='FlowerType')
print(x.head())

pca_iris = PCA(n_components=3).fit(iris.data) 
print(pca_iris) 
print(pca_iris.explained_variance_ratio_) 
print(pca_iris.components_) 
print(pca_iris.transform(iris.data))


skumulowana_wariancja = pca.explained_variance_ratio_.cumsum()
print("skumulowana wariancja", skumulowana_wariancja)

komponenty_n_95 = next()