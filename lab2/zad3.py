import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.preprocessing import MinMaxScaler, StandardScaler

iris = datasets.load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target

df_selected = df[['sepal length (cm)', 'sepal width (cm)', 'target']]

scaler_minmax = MinMaxScaler()
scaler_zscore = StandardScaler()

df_minmax = df_selected.copy()
df_minmax[['sepal length (cm)', 'sepal width (cm)']] = scaler_minmax.fit_transform(df_minmax[['sepal length (cm)', 'sepal width (cm)']])

df_zscore = df_selected.copy()
df_zscore[['sepal length (cm)', 'sepal width (cm)']] = scaler_zscore.fit_transform(df_zscore[['sepal length (cm)', 'sepal width (cm)']])

def plot_iris(df, title):
    plt.figure(figsize=(8, 6))
    for target, color in zip([0, 1, 2], ['r', 'g', 'b']):
        subset = df[df['target'] == target]
        plt.scatter(subset['sepal length (cm)'], subset['sepal width (cm)'], c=color, label=iris.target_names[target], edgecolor='k')
    plt.title(title)
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Sepal Width (cm)')
    plt.legend()
    plt.grid(True)
    plt.show()

plot_iris(df_selected, 'Oryginalne dane')
plot_iris(df_minmax, 'Znormalizowane dane (Min-Max)')
plot_iris(df_zscore, 'Zeskalowane dane (Z-Score)')

print("Statystyki dla oryginalnych danych:")
print(df_selected.describe())

print("\nStatystyki dla znormalizowanych danych (Min-Max):")
print(df_minmax.describe())

print("\nStatystyki dla zeskalowanych danych (Z-Score):")
print(df_zscore.describe())