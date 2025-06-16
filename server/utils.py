
import pickle
import os
import pandas as pd


def load_model(model_filename='heart_disease_model.pkl'):
    """Carrega o modelo de ML usando pickle."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(current_dir, '..', 'ml', model_filename)
    if not os.path.exists(model_path):
        raise FileNotFoundError("Model file not found")
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)
    return model


def convert_input_to_model_format(input_dict):
    # Cria DataFrame com uma linha
    df = pd.DataFrame([input_dict])

    # Mapas para variáveis categóricas binárias
    df['Sex'] = df['Sex'].map({'M': 1, 'F': 0})
    df['ExerciseAngina'] = df['ExerciseAngina'].map({'Y': 1, 'N': 0})

    # One-hot encoding para as demais
    df = pd.get_dummies(
        df, columns=['ChestPainType', 'RestingECG', 'ST_Slope'])

    # Garante todas as colunas do modelo, preenchendo com 0 se faltar
    colunas_modelo = [
        'Age', 'Sex', 'RestingBP', 'Cholesterol', 'FastingBS', 'MaxHR', 'ExerciseAngina', 'Oldpeak',
        'ChestPainType_ASY', 'ChestPainType_ATA', 'ChestPainType_NAP', 'ChestPainType_TA',
        'RestingECG_LVH', 'RestingECG_Normal', 'RestingECG_ST',
        'ST_Slope_Down', 'ST_Slope_Flat', 'ST_Slope_Up'
    ]
    df = df.reindex(columns=colunas_modelo, fill_value=0)

    return df.values[0].tolist()
