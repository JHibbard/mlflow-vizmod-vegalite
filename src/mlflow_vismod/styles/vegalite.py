"""

"""
# Standard Libraries
import os

# External Libraries
import mlflow.pyfunc


MODEL_DATA_SUBPATH = 'viz.html'

class Style(mlflow.pyfunc.PythonModel):
    """

    """
    def __init__(
            self,
            artifact_uri,
    ):
        self.artifact_uri = artifact_uri

    def __str__(self):
        """

        """
        return self.__repr__()

    def __repr__(self):
        """

        """
        return self.artifact_uri

    def _repr_html_(self):
        """

        """
        path = os.path.join(self.artifact_uri, MODEL_DATA_SUBPATH)
        with open(path, 'r') as html:
            data = html.read()
        return data

    def display(self, model_input):
        """

        """
        pass

    @staticmethod
    def save(model, path):
        """

        """
        model.save(os.path.join(path, MODEL_DATA_SUBPATH))
