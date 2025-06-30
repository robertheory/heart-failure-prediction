import os
import pandas as pd
from sklearn.model_selection import train_test_split
import pickle
import numpy as np


class Preprocessor:

    def __init__(self):
        """
        Initialize the Preprocessor class.
        This class is responsible for preprocessing data for machine learning models.
        """
        pass

    def train_test_split(self, dataset, test_size=0.2, seed=7):
        """
        Split the dataset into training and testing sets.

        :param dataset: The dataset to split
        :param test_size: Proportion of the dataset to include in the test split
        :param seed: Random seed for reproducibility
        :return: Tuple of training and testing sets
        """

        X_train, X_test, Y_train, Y_test = self.__holdout_prepare(
            dataset, test_size=test_size, seed=seed)

        return (X_train, X_test, Y_train, Y_test)

    def __holdout_prepare(self, dataset, test_size=0.2, seed=7):
        """
        Prepare the dataset for holdout validation.

        :param dataset: The dataset to prepare
        :param test_size: Proportion of the dataset to include in the test split
        :param seed: Random seed for reproducibility
        :return: Tuple of training and testing sets
        """
        X_train, X_test = self.train_test_split(
            dataset, test_size=test_size, seed=seed)
        return X_train, X_test

    def load_scaler(self, scaler_filename='heart_disease_scaler.pkl'):
        """Carrega o scaler de ML usando pickle."""
        current_dir = os.path.dirname(os.path.abspath(__file__))
        scaler_path = os.path.join(
            current_dir, '..', 'ml', scaler_filename)
        if not os.path.exists(scaler_path):
            raise FileNotFoundError("Scaler file not found")
        with open(scaler_path, 'rb') as scaler_file:
            scaler = pickle.load(scaler_file)
        return scaler

    def prepare_form(self, input_dict):
        """
        Prepare the input form data for prediction.

        :param form: Input form data
        :return: Processed input data as a numpy array
        """

        # Convert input form to a DataFrame
        X_input = pd.DataFrame([{
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

        # Map categorical variables to numerical values
        X_input['Sex'] = X_input['Sex'].map({'M': 1, 'F': 0})
        X_input['ExerciseAngina'] = X_input['ExerciseAngina'].map({
                                                                  'Y': 1, 'N': 0})

        # One-hot encoding for categorical variables
        X_input = pd.get_dummies(
            X_input,
            columns=['ChestPainType', 'RestingECG', 'ST_Slope']
        )

        # Ensure all expected columns are present
        expected_columns = [
            'Age', 'Sex', 'RestingBP', 'Cholesterol', 'FastingBS', 'MaxHR',
            'ExerciseAngina', 'Oldpeak',
            'ChestPainType_ASY', 'ChestPainType_ATA', 'ChestPainType_NAP', 'ChestPainType_TA',
            'RestingECG_LVH', 'RestingECG_Normal', 'RestingECG_ST',
            'ST_Slope_Down', 'ST_Slope_Flat', 'ST_Slope_Up'
        ]

        for col in expected_columns:
            if col not in X_input.columns:
                X_input[col] = 0

        # Sort columns to expected order
        X_input = X_input[expected_columns]

        # Convert to float
        X_input = X_input.astype(float)

        scaler = self.load_scaler()

        # Apply trained scaler
        rescaled_X_input = scaler.transform(X_input)

        return rescaled_X_input
