# Best Friends Animal Society Adoption Probability Prediction Model

## Description
Best Friends Animal Society is an organization based in the United States known for its efforts to promote pet adoption and reduce the number of animals euthanized in shelters.

## Request
The organization is seeking a solution to predict the probability of adoption for animals in shelters, aiming to increase their chances of finding new homes.
AdoptionSpeed is a metric to evaluate how fast a new animal will be adopted.


### Requirements

    python 3.7

    numpy==1.17.3
    pandas==1.1.5
    sklearn==1.0.0

### Running:

    To run the demo, execute:
        python predict.py 

    After running the script in that folder will be generated <prediction_results.csv> 
    The file has 'AdoptionSpeed_pred' column with the result value.

    The input is expected csv file in the same folder with a name <new_data.csv>. The file should have all features columns. 

### Training a Model:

    Before you run the training script for the first time, you must create dataset. The file <train_data.csv> should contain all features columns and target for prediction Churn.
    After running the script the "param_dict.pickle"  and "finalized_model.saw" will be created.
    Run the training script:
        python train.py

    The model accuracy is 92%
    There is no fraud check.


#### Scripts
The project includes several Python scripts:
- predict.py. Implements the prediction model using machine learning techniques. It loads the model and predicts adoption probabilities for animals based on input features.
- classifier-train.py. Develops and trains the machine learning model using a RandomForestClassifier. It utilizes GroupKFold cross-validation for evaluation and saves the finalized model.
- feature-engineering.py. Performs feature engineering tasks such as handling missing values, categorical encoding, and integer encoding.
- split-data. Splits the data to Train/Test data.