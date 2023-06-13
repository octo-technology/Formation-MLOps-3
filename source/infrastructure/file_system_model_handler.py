import os

import joblib

from models import MODEL_REGISTRY
from source.domain.port.model_handler import ModelHandler

MODEL_PATH = os.path.join(MODEL_REGISTRY, 'model.joblib')


class FilSystemModelHandler(ModelHandler):
    def save_model(self, model) -> None:
        joblib.dump(model, MODEL_PATH)

    def load_model(self):
        return joblib.load(MODEL_PATH)
