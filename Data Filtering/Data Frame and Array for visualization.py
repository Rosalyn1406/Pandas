import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

# Visualization using DataFrame (pandas)
df.plot(x='Name', kind='bar', title='Math Scores vs. Names')
plt.ylabel('Score')
plt.show()

# Visualization using NumPy array (matplotlib)
plt.bar(data['Name'], math_scores)
plt.title('Math Scores vs. Names')
plt.ylabel('Score')
plt.show()
