from pygments.lexers import graphviz
from sklearn.tree import DecisionTreeClassifier, export_graphviz, export_text
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report, ConfusionMatrixDisplay
from sklearn.preprocessing import StandardScaler
import pandas as pd
import matplotlib.pyplot as plt
import subprocess

TEST_SIZE = 0.1
MAX_DEPTH = 10
MIN_SAMPLES_SPLIT = 5
MIN_SAMPLES_LEAF = 5
MAX_FEATURES = 4


def loadData():
    data = pd.read_csv('treino_serv_controls.txt', sep=',', header=None)
    # testing now: SEC01-BP06
    data.columns = ["index", "trdparty", "ec2", "rds", "s3", "cloudfront", "lambda", "classificacao"]

    data.drop(columns=['index'], inplace=True)

    explicadores = data[["trdparty", "ec2", "rds", "s3", "cloudfront", "lambda"]]

    target = data[['classificacao']]

    print('Data shape:', data.shape)

    return explicadores, target


# for i in range(0, 100):
    # Load dataset
explicadores, target = loadData()

# Split dataset into training and testing sets
data_train, data_test, target_train, target_test = train_test_split(explicadores, target, test_size=TEST_SIZE)

data_test = data_test.values
data_train = data_train.values

# Normalização de dados
scaler = StandardScaler()
N_data_train = scaler.fit_transform(data_train)
N_data_test = scaler.transform(data_test)

# Train the Decision Tree using ID3 algorithm
tree = DecisionTreeClassifier(criterion="entropy", max_depth=MAX_DEPTH,
                              min_samples_split=MIN_SAMPLES_SPLIT,
                              min_samples_leaf=MIN_SAMPLES_LEAF, max_features=MAX_FEATURES)
tree.fit(N_data_train, target_train)

# Predict on test set
y_pred = tree.predict(N_data_test)

# plotcm = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(target_test, y_pred),
#                                 display_labels=['0', '1'])
# plotcm.plot()
# plt.show()

accuracy = tree.score(data_test, target_test)

print(classification_report(target_test, y_pred, ))

result_data = classification_report(target_test, y_pred, output_dict=True)

# Salvar resultado para futura comparacao
# file_object = open('results/resultsID3Class.txt', 'a')
# file_object.write(f'{result_data["accuracy"]}\n')
# file_object.close()

# Export the decision tree to a DOT file
export_graphviz(tree, out_file="decision_tree.dot",
                feature_names=explicadores.columns,
                class_names=["0", "1"],
                filled=True, rounded=True,
                special_characters=True)

# Convert the DOT file to a PNG image
subprocess.run(['dot', '-Tpng', 'decision_tree.dot', '-o', 'decision_tree.png'])

# Export the decision tree to text format
tree_rules = export_text(tree, feature_names=list(explicadores.columns))

# Print the decision tree rules
print(tree_rules)