from abc import ABC, abstractmethod

from source.domain.entities.model_type import ModelType


class ModelHandler(ABC):
    @abstractmethod
    def save_model(self, model) -> None:
        pass

    @abstractmethod
    def load_model(self, model: ModelType):
        pass
