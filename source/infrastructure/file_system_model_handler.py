import os

import joblib
import mlflow
from mlflow import MlflowException

from models import MODEL_REGISTRY
from source.domain.port.model_handler import ModelHandler

MODEL_PATH = os.path.join(MODEL_REGISTRY, 'model.joblib')


class FilSystemModelHandler(ModelHandler):
    def save_model(self, model) -> None:
        joblib.dump(model, MODEL_PATH)

    def load_model(self):
        try:
            return mlflow.pyfunc.load_model(model_uri=f"models:/customer/production")
        except MlflowException:
            return joblib.load(MODEL_PATH)
