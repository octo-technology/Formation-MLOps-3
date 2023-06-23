import pandas as pd
import pandera as pa

from source.domain.entities.prediction_schema import PredictionSchema
from source.domain.port.model_handler import ModelHandler
from source.domain.usecase.train_model import prepare_data

INFERENCE_COL = 'inference'


@pa.check_output(PredictionSchema)
def predict_model(df: pd.DataFrame, model_handler: ModelHandler) -> pd.DataFrame:
    model = model_handler.load_model()
    df_prepared = prepare_data(df)
    predictions = model.predict(df_prepared)
    return pd.DataFrame({INFERENCE_COL: predictions})
