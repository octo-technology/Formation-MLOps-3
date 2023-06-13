from abc import ABC, abstractmethod


class ModelHandler(ABC):
    @abstractmethod
    def save_model(self, model) -> None:
        pass

    @abstractmethod
    def load_model(self):
        pass
