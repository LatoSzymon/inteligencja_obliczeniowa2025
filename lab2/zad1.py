import pandas as uwu

#df = uwu.read_csv("c:/Users/szymo/repozytoria/int2025/inteligencja_obliczeniowa2025/lab2/iris1.csv")

df = uwu.read_csv("c:/Users/szymo/repozytoria/int2025/inteligencja_obliczeniowa2025/lab2/iris_with_errors.csv")
#print(df)

print(df.values)
print("Nazwy kolumn:")
print(df.columns)

braki = df.isnull().sum()
print("Braki danych:")
print(braki)

print("Statystyki z błędami:")
print(df.describe(include='all'))

for k in df.select_dtypes(include=['float64', 'int64']).columns:
    srednia = df[k].mean()
    for i in range(len(df[k])):
        if df[k].iloc[i] < 0 or df[k].iloc[i] > 15:
            df[k].iloc[i] = srednia

rasy_panow = ["Setosa", "Versicolor", "Virginica"]
rasy_gorsze = df[~df['variety'].isin(rasy_panow)]['variety'].unique()
print("Gatunki niewłaściwe i zdecydowanie nie na miejscu:")
print(rasy_gorsze)

df['variety'] = df['variety'].replace(rasy_gorsze, "Setosa")

df.to_csv("c:/Users/szymo/repozytoria/int2025/inteligencja_obliczeniowa2025/lab2/iris_cleaned.csv", index=False)



