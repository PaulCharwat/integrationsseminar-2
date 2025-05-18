import pandas as pd

# Load data from the CSV file (specify the correct delimiter)
data2 = pd.read_csv('2.csv', delimiter=';')

# Reference the "Temperatur" column
x2 = data2["Temperatur"]
y2 = data2["Verbrauch"]

# Calculate correlation
correlation2 = x2.corr(y2)
print("Correlation for Hypotheses 2:", correlation2)