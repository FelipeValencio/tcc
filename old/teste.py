from sklearn.multioutput import MultiOutputClassifier
from sklearn.tree import DecisionTreeClassifier

import pandas as pd

df = pd.read_csv('file_name.csv')

print(df)

# Initialize base classifier
base_classifier = DecisionTreeClassifier()

# Wrap base classifier in MultiOutputClassifier to handle multilabel classification
multi_label_classifier = MultiOutputClassifier(base_classifier)

