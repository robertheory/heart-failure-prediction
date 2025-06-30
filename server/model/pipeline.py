import pickle


class Pipeline:
    """
    Classe Pipeline para carregar o modelo e o scaler, e fazer previsões.
    """

    def __init__(self):
        self.pipeline = None

    def load_pipeline(self, path):
        """
        Loads the pipeline
        """
        with open(path, 'rb') as file:
            self.pipeline = pickle.load(file)

        return self.pipeline
