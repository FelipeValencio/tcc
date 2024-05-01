import pandas as pd

df = pd.read_csv('datasets/apenasRespostas.csv', index_col=False)

for i, row in df.iterrows():
    if df.at[i, 'dev-08'] == 0:
        df.at[i, 'SEC04-BP02'] = 1
        if df.at[i, 'dev-11'] == 0:
            df.at[i, 'SEC04-BP03'] = 1

    if df.at[i, 'dev-10'] == 1:
        df.at[i, 'SEC02-BP03'] = 1

    if df.at[i, 'dev-09'] == 1:
        df.at[i, 'SEC11-BP03'] = 1

    if df.at[i, 'dev-05'] == 1:
        if df.at[i, 'dev-06'] == 0:
            df.at[i, 'SEC02-BP05'] = 1

    if df.at[i, 'dev-03'] == 1:
        df.at[i, 'SEC03-BP08'] = 1
        df.at[i, 'SEC03-BP07'] = 1

    if df.at[i, 'dev-04'] == 1:
        df.at[i, 'SEC02-BP02'] = 1

    if df.at[i, 'dev-01'] == 1:
        df.at[i, 'SEC01-BP06'] = 1
        df.at[i, 'SEC11-BP01'] = 1
        df.at[i, 'SEC11-BP02'] = 1
        df.at[i, 'SEC11-BP03'] = 1
        df.at[i, 'SEC11-BP04'] = 1
        df.at[i, 'SEC11-BP06'] = 1
        df.at[i, 'SEC11-BP07'] = 1
        df.at[i, 'SEC11-BP08'] = 1
        if df.at[i, 'dev-07'] == 1:
            df.at[i, 'SEC11-BP05'] = 1
        if df.at[i, 'dev-02'] == 1:
            df.at[i, 'SEC01-BP01'] = 1

# df = df.fillna(
#     {'SEC01-BP01': 0, 'SEC01-BP06': 0, 'SEC02-BP02': 0, 'SEC02-BP03': 0, 'SEC02-BP05': 0, 'SEC03-BP07': 0,
#      'SEC03-BP08': 0, 'SEC04-BP02': 0,
#      'SEC04-BP03': 0, 'SEC11-BP01': 0, 'SEC11-BP02': 0, 'SEC11-BP03': 0, 'SEC11-BP04': 0,
#      'SEC11-BP05': 0, 'SEC11-BP06': 0,
#      'SEC11-BP07': 0, 'SEC11-BP08': 0})

df.fillna(0, inplace=True)

df = df.astype(int)

df.to_csv("datasetNovo.csv", sep=',', encoding='utf-8', index=False)
