from model import *

loader = Loader()
model = Model()
evaluator = Evaluator()
preprocessor = Preprocessor()
pipeline = Pipeline()

data_url = './ml/heart.csv'
attributes = [
    'Age', 'Sex', 'RestingBP', 'Cholesterol', 'FastingBS', 'MaxHR',
    'ExerciseAngina', 'Oldpeak',
    'ChestPainType_ASY', 'ChestPainType_ATA', 'ChestPainType_NAP', 'ChestPainType_TA',
    'RestingECG_LVH', 'RestingECG_Normal', 'RestingECG_ST',
    'ST_Slope_Down', 'ST_Slope_Flat', 'ST_Slope_Up'
]

dataset = loader.load(data_url, attributes)
array = dataset.values

X, y = preprocessor.train_test_split(array, test_size=0.2, seed=42)
X = preprocessor.scale(X)

TARGET_ACCURACY = 0.8


def test_model_nb():
    nb_path = './ml/heart_disease_model.pkl'

    model_nb = model.load_model(nb_path)

    accuracy = evaluator.evaluate(model_nb, X, y)

    print(f"Naive Bayes Model Accuracy: {accuracy}")

    assert accuracy >= TARGET_ACCURACY, f"Naive Bayes model accuracy {accuracy} is below target {TARGET_ACCURACY}"
