import pickle
import pandas as pd
import numpy as np
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 500)

# custom files
import columns

try:
    ds = pd.read_csv("D:/programming/information-technologies-of-smart-systems/practice/practice-5/data/new_data.csv")
    print('new data size', ds.shape)
except FileNotFoundError:
    print("Error: File not found!")
    exit()

# feature engineering
try:
    param_dict = pickle.load(open('D:/programming/information-technologies-of-smart-systems/practice/practice-5/src/param_dict.pickle', 'rb'))
except FileNotFoundError:
    print("Error: Parameter dictionary file not found!")
    exit()

# Missing data imputation
def impute_na(df, variable, value):
#     df[variable] = df[variable].replace(np.NaN, value)
    return df[variable].fillna(value)

# Let's read a dict and impute mode values
for column in columns.mode_impute_columns:
    ds[column] = impute_na(ds, column, param_dict['mode_impute_values'][column])

# Let's read a dict and impute mode values
for column in columns.outlier_columns:
    ds[column] = impute_na(ds, column, param_dict['outlier_values'][column])

# Categorical encoding
for column in columns.cat_columns[0:]:
    ds[column] = ds[column].map(param_dict['map_dicts'][column])
    # to encoding missing (new) categories
    ds[column] = impute_na(ds, column, max(param_dict['map_dicts'][column].values())+1)


# Define target and features columns
X = ds[columns.X_columns]

# load the model and predict
try:
    rf = pickle.load(open('D://programming//information-technologies-of-smart-systems//practice//practice-5//models/finalized_model.sav', 'rb'))
except FileNotFoundError:
    print("Error: Model file not found!")
    exit()

try:
    y_pred = rf.predict(X)
    ds['AdoptionSpeed_pred'] = rf.predict(X)
    ds.to_csv('D:/programming/information-technologies-of-smart-systems/practice/practice-5/data/prediction_results.csv', index=False)
except Exception as e:
    print("Error occurred while predicting:", e)