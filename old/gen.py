import pandas as pd
import numpy as np

# Provided entries
entries = [
    [1, 0, 1, 0, 1, 0, 1, 1],
    [2, 1, 1, 0, 0, 1, 0, 1],
    [3, 0, 1, 1, 0, 0, 1, 1],
    [4, 0, 0, 0, 1, 0, 0, 0],
    [5, 0, 0, 1, 0, 1, 1, 1],
    [6, 0, 0, 0, 1, 1, 0, 1],
    [7, 0, 1, 0, 0, 0, 0, 1],
    [8, 0, 0, 1, 0, 0, 0, 0],
    [9, 0, 0, 0, 0, 1, 0, 1],
    [10, 0, 0, 0, 0, 0, 1, 1]
]

# Convert entries to DataFrame
df = pd.DataFrame(entries, columns=['index', 'feat1', 'feat2', 'feat3', 'feat4', 'feat5', 'feat6', 'feat7'])

# Number of additional examples to generate
num_examples = 1000

# Generate additional examples
additional_examples = []
for i in range(num_examples):
    # Randomly modify one of the features in each example
    modified_example = df.iloc[np.random.choice(len(df)), :].copy()
    modified_feature = np.random.choice(df.columns[1:])
    modified_example[modified_feature] = np.random.randint(2)  # randomly set the feature to 0 or 1
    additional_examples.append(modified_example)

# Convert additional examples to DataFrame
additional_df = pd.DataFrame(additional_examples)

# Display the first few rows of the additional examples
print(additional_df.head())

# Save the additional examples to a CSV file
additional_df.to_csv('additional_examples.csv', index=False)
