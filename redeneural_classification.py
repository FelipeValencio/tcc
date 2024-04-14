import os
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report, multilabel_confusion_matrix
import matplotlib.pyplot as plt
import numpy as np

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

TEST_SIZE = 0.3
EPOCHS = 100
LEARNING_RATE = 0.03
ACTV_FUNC = 'relu'
# OPTIMIZER = SGD(learning_rate=LEARNING_RATE)
OPTIMIZER = 'adam'


def loadData():
    data = pd.read_csv('dataframe_teste.csv')

    data.columns = ['dev-01', 'dev-02', 'dev-03', 'dev-04', 'dev-05', 'dev-06', 'dev-07', 'dev-08', 'dev-09', 'dev-10',
                    'dev-11', 'SEC01-BP01', 'SEC01-BP06', 'SEC02-BP02', 'SEC02-BP03', 'SEC02-BP05', 'SEC03-BP07',
                    'SEC03-BP08', 'SEC04-BP02', 'SEC04-BP03', 'SEC11-BP01', 'SEC11-BP02', 'SEC11-BP03', 'SEC11-BP04',
                    'SEC11-BP05', 'SEC11-BP06', 'SEC11-BP07', 'SEC11-BP08']

    explicadores = data[
        ['dev-01', 'dev-02', 'dev-03', 'dev-04', 'dev-05', 'dev-06', 'dev-07', 'dev-08', 'dev-09', 'dev-10',
                    'dev-11',]]

    target = data[['SEC01-BP01', 'SEC01-BP06', 'SEC02-BP02', 'SEC02-BP03', 'SEC02-BP05', 'SEC03-BP07',
                    'SEC03-BP08', 'SEC04-BP02', 'SEC04-BP03', 'SEC11-BP01', 'SEC11-BP02', 'SEC11-BP03', 'SEC11-BP04',
                    'SEC11-BP05', 'SEC11-BP06', 'SEC11-BP07', 'SEC11-BP08']]

    print('Data shape:', data.shape)

    print(explicadores)
    print(target)

    return explicadores, target


explicadores, target = loadData()

# Split dataset into training and testing sets
data_train, data_test, target_train, target_test = train_test_split(explicadores, target, test_size=TEST_SIZE, random_state=42)

# Define the model architecture
model = Sequential()
# cada linha eh uma camada, o primeiro parametro eh a quantidade de nos
model.add(Dense(11, input_dim=11, activation=ACTV_FUNC))
model.add(Dense(17, activation='sigmoid'))

# Compile the model
model.compile(loss='binary_crossentropy', optimizer=OPTIMIZER, metrics=['accuracy'])

# Fit the model to the data
model.fit(data_train, target_train, epochs=EPOCHS)

# Evaluate the model on some test data
y_pred = model.predict(data_test)
y_pred_binary = (y_pred > 0.5).astype(int)

# # Calculate confusion matrix
# conf_matrix = multilabel_confusion_matrix(target_test, y_pred_binary)
#
# # Display confusion matrix
# for i, (label_name, matrix) in enumerate(zip(target.columns, conf_matrix)):
#     print(f"Confusion Matrix for Label '{label_name}':")
#     print(matrix)
#     print()
#
# # Display predicted probabilities and binary labels for each test input
# for i in range(len(data_test)):
#     print(f"Test Input {i + 1}:")
#     print("Predicted Probabilities:")
#     print(y_pred[i])
#     print("Binary Labels (Predicted):")
#     print(y_pred_binary[i])
#     print("True Labels (Actual):")
#     print(target_test.iloc[i].values)
#     print()  # Add blank line for separation

# plotcm = ConfusionMatrixDisplay(
#     confusion_matrix=confusion_matrix(target_test, y_pred),
#     display_labels=['SEC01-BP01', 'SEC01-BP06', 'SEC02-BP02', 'SEC02-BP03', 'SEC02-BP05', 'SEC03-BP07',
#                     'SEC03-BP08', 'SEC04-BP02', 'SEC04-BP03', 'SEC11-BP01', 'SEC11-BP02', 'SEC11-BP03', 'SEC11-BP04',
#                     'SEC11-BP05', 'SEC11-BP06', 'SEC11-BP07', 'SEC11-BP08']
# )
#
# plotcm.plot()

# class_report = classification_report(target_test, y_pred)
#
# print(class_report)

# # Salvar resultado para futura comparacao
# file_object = open('results/resultsRNClass.txt', 'a')
# file_object.write(f'epochs: {EPOCHS}, layers: {len(model.layers)}, '
#                   f'LEARNING_RATE: {LEARNING_RATE}, '
#                   f'test_size: {TEST_SIZE}, ACTV_FUNC: {ACTV_FUNC}\n')
# file_object.write(class_report + '\n')
# file_object.close()

plt.show()
