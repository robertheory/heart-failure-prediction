import pickle
import os
import numpy as np
import pandas as pd

from schemas.predict import ModelInput, PredictInput


def load_scaler(scaler_filename='heart_disease_scaler.pkl'):
    """Carrega o scaler de ML usando pickle."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    scaler_path = os.path.join(current_dir, '..', 'ml', scaler_filename)
    if not os.path.exists(scaler_path):
        raise FileNotFoundError("Scaler file not found")
    with open(scaler_path, 'rb') as scaler_file:
        scaler = pickle.load(scaler_file)
    return scaler


def load_model(model_filename='heart_disease_model.pkl'):
    """Carrega o modelo de ML usando pickle."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(current_dir, '..', 'ml', model_filename)
    if not os.path.exists(model_path):
        raise FileNotFoundError("Model file not found")
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)
    return model


def convert_input_to_model_format(input_dict: PredictInput) -> np.ndarray:
    """
    Converte o input do usuário para o formato esperado pelo modelo,
    aplicando o mesmo pré-processamento usado no treinamento.
    """
    scaler = load_scaler()

    # Cria DataFrame com os dados de entrada
    entrada = pd.DataFrame([{
        'Age': input_dict.Age,
        'Sex': input_dict.Sex,
        'RestingBP': input_dict.RestingBP,
        'Cholesterol': input_dict.Cholesterol,
        'FastingBS': 1 if input_dict.FastingBS == 'Y' else 0,
        'MaxHR': input_dict.MaxHR,
        'ExerciseAngina': input_dict.ExerciseAngina,
        'Oldpeak': input_dict.Oldpeak,
        'ChestPainType': input_dict.ChestPainType,
        'RestingECG': input_dict.RestingECG,
        'ST_Slope': input_dict.ST_Slope
    }])

    # Mapeia variáveis categóricas conforme treinamento
    entrada['Sex'] = entrada['Sex'].map({'M': 1, 'F': 0})
    entrada['ExerciseAngina'] = entrada['ExerciseAngina'].map({'Y': 1, 'N': 0})

    # One-hot encoding para as demais variáveis categóricas
    entrada = pd.get_dummies(
        entrada,
        columns=['ChestPainType', 'RestingECG', 'ST_Slope']
    )

    # Garante que todas as colunas esperadas estejam presentes
    expected_columns = [
        'Age', 'Sex', 'RestingBP', 'Cholesterol', 'FastingBS', 'MaxHR',
        'ExerciseAngina', 'Oldpeak',
        'ChestPainType_ASY', 'ChestPainType_ATA', 'ChestPainType_NAP', 'ChestPainType_TA',
        'RestingECG_LVH', 'RestingECG_Normal', 'RestingECG_ST',
        'ST_Slope_Down', 'ST_Slope_Flat', 'ST_Slope_Up'
    ]
    for col in expected_columns:
        if col not in entrada.columns:
            entrada[col] = 0

    # Ordena as colunas na ordem esperada
    entrada = entrada[expected_columns]

    # Converte para float
    entrada = entrada.astype(float)

    # Aplica o scaler treinado
    rescaled_entrada = scaler.transform(entrada)

    return rescaled_entrada
