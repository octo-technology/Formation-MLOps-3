import logging
import os

import joblib
import mlflow
from mlflow import MlflowException

from models import MODEL_REGISTRY
from source.domain.entities.model_type import ModelType
from source.domain.port.model_handler import ModelHandler

MODEL_PATH = os.path.join(MODEL_REGISTRY, 'model.joblib')


class FilSystemModelHandler(ModelHandler):
    def save_model(self, model) -> None:
        joblib.dump(model, MODEL_PATH)

    def load_model(self, model: ModelType):
        try:
            model = mlflow.pyfunc.load_model(model_uri=f"models:/customer/{model}")
            logging.info('Successfully loaded model from MLflow')
            return model
        except MlflowException:
            logging.info('Failed to load model from MLflow, loading default model')
            return joblib.load(MODEL_PATH)
