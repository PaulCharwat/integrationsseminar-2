import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import pandas as pd

# Hypotheses 1
data1 = pd.read_csv('1.csv')
x1 = data1["Anteil EE"]
y1 = data1["Preis"]
plt.figure()
plt.scatter(x1, y1)
plt.title("Hypothesis 1: Anteil EE vs Preis")
plt.xlabel("Anteil EE")
plt.ylabel("Preis")
plt.show()

# Hypotheses 2
data2 = pd.read_csv('2.csv', delimiter=';')
x2 = data2["Temperatur"]
y2 = data2["Verbrauch"]
plt.figure()
plt.scatter(x2, y2)
plt.title("Hypothesis 2: Temperatur vs Verbrauch")
plt.xlabel("Temperatur")
plt.ylabel("Verbrauch")
plt.show()

# Hypotheses 3
data3 = pd.read_csv('3.csv', delimiter=';')
x3 = data3["Temperatur"]
y3 = data3["Anteil VE"]
plt.figure()
plt.scatter(x3, y3)
plt.title("Hypothesis 3: Temperatur vs Anteil VE")
plt.xlabel("Temperatur")
plt.ylabel("Anteil VE")
plt.show()