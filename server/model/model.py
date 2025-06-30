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
        try:
            with open(model_path, 'rb') as file:
                self.model = pickle.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Model file not found at {model_path}.")
        except Exception as e:
            raise RuntimeError(
                f"An error occurred while loading the model: {e}")

    def predict(self, X_input):
        """
        Make predictions using the loaded model.

        :param X_input: Input data for prediction
        :return: Predictions made by the model
        :raises RuntimeError: If no model is loaded
        """
        if self.model is None:
            raise RuntimeError(
                "No model loaded. Please load a model before making predictions.")

        return self.model.predict(X_input)
