from scipy.stats import pearsonr
import pandas as pd

# Hypotheses 1
data1 = pd.read_csv('1.csv')
x1 = data1["Anteil EE"]
y1 = data1["Preis"]
correlation1 = x1.corr(y1)
print("Correlation for Hypotheses 1:", correlation1)
print(pearsonr(x1, y1))

# Hypotheses 2
data2 = pd.read_csv('2.csv', delimiter=';')
x2 = data2["Temperatur"]
y2 = data2["Verbrauch"]
correlation2 = x2.corr(y2)
print("Correlation for Hypotheses 2:", correlation2)
print(pearsonr(x2, y2))

# Hypotheses 3
data3 = pd.read_csv('3.csv', delimiter=';')
x3 = data3["Temperatur"]
y3 = data3["Anteil VE"]
correlation3 = x3.corr(y3)
print("Correlation for Hypotheses 3:", correlation3)
print(pearsonr(x3, y3))