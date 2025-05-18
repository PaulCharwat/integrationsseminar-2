import pandas as pd

# Load data from the CSV file (header present)
df = pd.read_csv('1.csv')

# Extract columns
x = df.iloc[:, 1]  # Second column (Großhandelspreise)
y = df.iloc[:, 2]  # Third column (Anteil EE an der Last)

# Calculate correlation
correlation1 = x.corr(y)
print("Correlation for Hypotheses 1:", correlation1)

