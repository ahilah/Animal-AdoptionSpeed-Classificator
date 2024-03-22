mode_impute_columns = ['Gender']

outlier_columns = ['MaturitySize', 'BreedName_x', 'BreedName_y', 'ColorName']

cat_columns = ['StateName_x', 'ColorName_x', 'ColorName_y', 'ColorName', 'BreedName_x', 'BreedName_y']

y_column = ['AdoptionSpeed'] # target variable
X_columns = ['Type', 'Age', 'Gender', 'MaturitySize', 'FurLength', 'Vaccinated', 'Dewormed',
              'Sterilized', 'Health', 'Quantity', 'Fee', 'State', 'VideoAmt', 'PhotoAmt',
              'ColorName_x', 'ColorName_y', 'ColorName', 'BreedName_x', 'BreedName_y', 'StateName_x']