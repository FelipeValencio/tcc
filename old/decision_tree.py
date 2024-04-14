import seaborn as sns
from sklearn import tree
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

df = pd.read_csv('../dataframe_teste.csv')

X = df[
    ['dev-01', 'dev-02', 'dev-03', 'dev-04', 'dev-05', 'dev-06', 'dev-07', 'dev-08', 'dev-09', 'dev-10', 'dev-11']]
Y = df["survived"]

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.7, random_state=42)

tree_model = tree.DecisionTreeClassifier()

tree_model.fit(X_train, y_train)

fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(8, 8), dpi=150)

tree.plot_tree(tree_model, feature_names=X.columns, class_names=["1", "0"])

plt.plot()
