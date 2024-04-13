import itertools

# Define the list of column names
columns = [
    'dev-01', 'dev-02', 'dev-03', 'dev-04', 'dev-05', 'dev-06', 'dev-07', 'dev-08', 'dev-09', 'dev-10', 'dev-11'
    # 'serv-01', 'serv-02', 'serv-03', 'serv-04', 'serv-05', 'serv-06', 'serv-07', 'serv-08', 'serv-09', 'serv-10',
    # 'serv-11',
    # 'func-01', 'func-02', 'func-03', 'func-04',
    # 'nat-01', 'nat-02', 'nat-03', 'nat-04', 'nat-05', 'nat-06'
]

# Generate all possible combinations of "Yes" and "No" for the columns
combinations = list(itertools.product([1, 0], repeat=len(columns)))

# Print the combinations
for i, combination in enumerate(combinations, 1):
    print(f"{dict(zip(columns, combination))},")
