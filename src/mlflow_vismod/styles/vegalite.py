"""

"""
# Standard Libraries
import os

# External Libraries
import mlflow.pyfunc


MODEL_DATA_SUBPATH = 'viz.html'

class Style(mlflow.pyfunc.PythonModel):
    """
        local_model_path=local_model_path,
        model_dir_subpath=model_dir_subpath,

        # self.local_model_path = kwargs['local_model_path']
        # self.model_dir_subpath = kwargs['model_dir_subpath']
    """
    def __init__(
            self,
            artifact_uri,
    ):
        self.artifact_uri = artifact_uri

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        # return f'Style(local_model_path={self.local_model_path}, model_dir_subpath={self.model_dir_subpath})'
        return self.artifact_uri

    def _repr_html_(self):
        path = os.path.join(self.artifact_uri, MODEL_DATA_SUBPATH)
        with open(path, 'r') as html:
            data = html.read()
        return data

    def display(self, model_input):
        pass

    @staticmethod
    def save(model, path):
        model.save(os.path.join(path, MODEL_DATA_SUBPATH))

    """
    def display(self, *kwargs):
        local_spec_path = os.path.join(self.local_model_path, self.model_dir_subpath, 'spec.json')
        local_conf_path = os.path.join(self.local_model_path, self.model_dir_subpath, 'config.json')
        with open(local_spec_path, 'r') as file:
            spec = json.load(file)

        with open(local_conf_path, 'r') as file:
            config = json.load(file)

        return altair_viewer.display(spec)

    def get_raw_io(self):
        path = pathlib.Path(self.local_model_path, self.model_dir_subpath)
        paths = [p for p in path.glob('*') if p.is_file()]
        return {str(p).replace(self.local_model_path, ''): io.BytesIO(open(p, 'rb').read()) for p in paths}
    """
