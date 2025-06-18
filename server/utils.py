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


def convert_input_to_model_format(input_dict: PredictInput) -> pd.DataFrame:
    scaler = load_scaler()

    # Convertendo o input para o formato esperado pelo modelo
    data = {
        'Age': [input_dict.Age],
        'Sex': [1 if input_dict.Sex == 'M' else 0],
        'RestingBP': [input_dict.RestingBP],
        'Cholesterol': [input_dict.Cholesterol],
        'FastingBS': [1 if input_dict.FastingBS == 'Y' else 0],
        'MaxHR': [input_dict.MaxHR],
        'ExerciseAngina': [1 if input_dict.ExerciseAngina == 'Y' else 0],
        'Oldpeak': [input_dict.Oldpeak],
        'ChestPainType_ASY': [1 if input_dict.ChestPainType == 'ASY' else 0],
        'ChestPainType_ATA': [1 if input_dict.ChestPainType == 'ATA' else 0],
        'ChestPainType_NAP': [1 if input_dict.ChestPainType == 'NAP' else 0],
        'ChestPainType_TA': [1 if input_dict.ChestPainType == 'TA' else 0],
        'RestingECG_LVH': [1 if input_dict.RestingECG == 'LVH' else 0],
        'RestingECG_Normal': [1 if input_dict.RestingECG == 'Normal' else 0],
        'RestingECG_ST': [1 if input_dict.RestingECG == 'ST' else 0],
        'ST_Slope_Down': [1 if input_dict.ST_Slope == 'Down' else 0],
        'ST_Slope_Flat': [1 if input_dict.ST_Slope == 'Flat' else 0],
        'ST_Slope_Up': [1 if input_dict.ST_Slope == 'Up' else 0],
    }

    atributos = ['Age', 'Sex', 'RestingBP', 'Cholesterol', 'FastingBS', 'MaxHR', 'ExerciseAngina', 'Oldpeak', 'ChestPainType_ASY', 'ChestPainType_ATA',
                 'ChestPainType_NAP', 'ChestPainType_TA', 'RestingECG_LVH', 'RestingECG_Normal', 'RestingECG_ST', 'ST_Slope_Down', 'ST_Slope_Flat', 'ST_Slope_Up']
    entrada = pd.DataFrame(data, columns=atributos)

    # Convertendo o DataFrame para um array NumPy de tipo float64
    array_entrada = entrada.values.astype(np.float64)
    # Padronização nos dados de entrada usando o scaler utilizado em X
    rescaledEntradaX = scaler.transform(array_entrada)

    return rescaledEntradaX
