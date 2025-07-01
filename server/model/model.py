import pickle


class Model:
    def __init__(self):
        """
        Initialize the Model class.
        This class is responsible for loading and saving machine learning models.
        """
        self.model = None

    def load_model(self, model_path: str):
        """
        Load a machine learning model from the specified path.

        :param model_path: Path to the saved model file
        :raises FileNotFoundError: If the model file does not exist
        :raises RuntimeError: If there is an error loading the model
        """
        if model_path.endswith('.pkl'):
            with open(model_path, 'rb') as file:
                self.model = pickle.load(file)
        else:
            raise Exception('Formato de arquivo não suportado')
        return self.model

    def predict(self, X_input):
        """
        Make predictions using the loaded model.

        :param X_input: Input data for prediction
        :return: Predictions made by the model
        :raises RuntimeError: If no model is loaded
        """
        if self.model is None:
            raise Exception(
                'Model not loaded. Please load a model before making predictions.')
        diagnosis = self.model.predict(X_input)
        return diagnosis
