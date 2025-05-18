import pandas as pd

# Hypotheses 1

# Load data from the CSV file (header present)
data1 = pd.read_csv('1.csv')

# Extract columns
x1 = data1["Anteil EE"]
y1 = data1["Preis"]

# Calculate correlation
correlation1 = x1.corr(y1)
print("Correlation for Hypotheses 1:", correlation1)


# Hypotheses 2

# Load data from the CSV file (specify the correct delimiter)
data2 = pd.read_csv('2.csv', delimiter=';')

# Reference the "Temperatur" column
x2 = data2["Temperatur"]
y2 = data2["Verbrauch"]

# Calculate correlation
correlation2 = x2.corr(y2)
print("Correlation for Hypotheses 2:", correlation2)


# Hypotheses 3

# Load data from the CSV file (specify the correct delimiter)
data3 = pd.read_csv('3.csv', delimiter=';')

# Reference the "Temperatur" column
x3 = data3["Temperatur"]
y3 = data3["Anteil VE"]

# Calculate correlation
correlation3 = x3.corr(y3)
print("Correlation for Hypotheses 3:", correlation3)