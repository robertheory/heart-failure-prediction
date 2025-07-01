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

dataset['Sex'] = dataset['Sex'].map({'M': 1, 'F': 0})
dataset['ExerciseAngina'] = dataset['ExerciseAngina'].map({'Y': 1, 'N': 0})

dataset = pd.get_dummies(
    dataset, columns=['ChestPainType', 'RestingECG', 'ST_Slope'])

dataset = dataset.astype(float)

X = dataset.drop('HeartDisease', axis=1)  # Features
y = dataset['HeartDisease']  # Target

TARGET_ACCURACY = 0.65


def test_model_cart():
    model_path = './ml/models/heart_disease_model_cart.pkl'

    ml_model = model.load_model(model_path)

    accuracy = evaluator.evaluate(ml_model, X, y)

    assert accuracy >= TARGET_ACCURACY, f"CART model accuracy {accuracy} is below target {TARGET_ACCURACY}"


def test_model_knn():
    model_path = './ml/models/heart_disease_model_knn.pkl'

    ml_model = model.load_model(model_path)

    accuracy = evaluator.evaluate(ml_model, X, y)

    assert accuracy >= TARGET_ACCURACY, f"KNN model accuracy {accuracy} is below target {TARGET_ACCURACY}"


def test_model_nb():
    model_path = './ml/models/heart_disease_model_nb.pkl'

    ml_model = model.load_model(model_path)

    accuracy = evaluator.evaluate(ml_model, X, y)

    assert accuracy >= TARGET_ACCURACY, f"Naive Bayes model accuracy {accuracy} is below target {TARGET_ACCURACY}"


def test_model_svm():
    model_path = './ml/models/heart_disease_model_svm.pkl'

    ml_model = model.load_model(model_path)

    accuracy = evaluator.evaluate(ml_model, X, y)

    assert accuracy >= TARGET_ACCURACY, f"SVM model accuracy {accuracy} is below target {TARGET_ACCURACY}"
