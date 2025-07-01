import pandas as pd
from model import *

loader = Loader()
model = Model()
evaluator = Evaluator()
preprocessor = Preprocessor()
pipeline = Pipeline()

data_url = './ml/heart.csv'

attributes = [
    'Age',
    'Sex',
    'RestingBP',
    'Cholesterol',
    'FastingBS',
    'MaxHR',
    'ExerciseAngina',
    'Oldpeak',
    'ChestPainType',
    'RestingECG',
    'ST_Slope',
    'HeartDisease'
]

dataset = loader.load(data_url, attributes)

# Codifica variáveis categóricas
dataset['Sex'] = dataset['Sex'].map({'M': 1, 'F': 0})
dataset['ExerciseAngina'] = dataset['ExerciseAngina'].map({'Y': 1, 'N': 0})

# One-hot encoding para as demais
dataset = pd.get_dummies(
    dataset, columns=['ChestPainType', 'RestingECG', 'ST_Slope'])

# Passa os dados para o formato float
dataset = dataset.astype(float)

X = dataset.drop('HeartDisease', axis=1)  # Features
y = dataset['HeartDisease']  # Target

TARGET_ACCURACY = 0.8


def test_model_nb():
    nb_path = './ml/heart_disease_model.pkl'

    model_nb = model.load_model(nb_path)

    accuracy = evaluator.evaluate(model_nb, X, y)

    assert accuracy >= TARGET_ACCURACY, f"Naive Bayes model accuracy {accuracy} is below target {TARGET_ACCURACY}"
