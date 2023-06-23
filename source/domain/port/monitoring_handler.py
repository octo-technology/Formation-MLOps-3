from abc import ABC, abstractmethod

import pandas as pd


class MonitoringHandler(ABC):

    @abstractmethod
    def save_inference(self, inference_df: pd.DataFrame) -> None:
        pass
