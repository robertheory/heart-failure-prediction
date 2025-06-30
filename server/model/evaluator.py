from sklearn.metrics import accuracy_score


class Evaluator:
    def __init__(self):
        """
        Initialize the Evaluator class.
        This class is responsible for evaluating the performance of a machine learning model.
        """
        pass

    def evaluate(self, model, X_test, y_test):
        """
        Evaluate the model on the test set and return the accuracy.

        :param model: Trained machine learning model
        :param X_test: Test features
        :param y_test: True labels for the test set
        :return: Accuracy of the model on the test set
        """
        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        return accuracy
