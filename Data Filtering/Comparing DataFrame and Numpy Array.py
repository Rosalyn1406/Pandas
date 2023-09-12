import pandas as pd
import numpy as np

# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
    'Math_Score': [85, 70, 90, 60, 75],
    'Science_Score': [92, 88, 78, 82, 95]
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Create a NumPy array from the math scores
math_scores = np.array(data['Math_Score'])

# Data Manipulation
print("DataFrame:")
print(df)
print("\nNumPy Array:")
print(math_scores)

# Accessing Data
print("\nAccessing data:")
print("DataFrame:")
print(df['Name'])
print("\nNumPy Array:")
print(math_scores[0])

# Filtering Data
print("\nFiltering data:")
print("DataFrame:")
print(df[df['Math_Score'] > 80])
print("\nNumPy Array:")
print(math_scores[math_scores > 80])

# Aggregation
print("\nAggregation:")
print("DataFrame:")
print(df.mean())
print("\nNumPy Array:")
print(np.mean(math_scores))


