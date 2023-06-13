import pandas as pd

from source.domain.port.model_handler import ModelHandler
from source.domain.usecase.train_model import prepare_data, DataSetColumns


def predict_model(df: pd.DataFrame, model_handler: ModelHandler) -> pd.DataFrame:
    model = model_handler.load_model()
    df_prepared = prepare_data(df)
    return model.predict(df_prepared[[DataSetColumns.age, 'education_level']])
