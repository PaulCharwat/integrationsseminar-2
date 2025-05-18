import pandas as pd
import matplotlib.pyplot as plt

# Load data from the CSV file (specify the correct delimiter)
data3 = pd.read_csv('3.csv', delimiter=';')

# Reference the "Temperatur" column
x3 = data3["Temperatur"]
y3 = data3["Anteil VE"]

# Calculate correlation
correlation3 = x3.corr(y3)
print("Correlation for Hypotheses 3:", correlation3)
