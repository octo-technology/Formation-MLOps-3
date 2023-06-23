import pandas as pd

from source.domain.port.monitoring_handler import MonitoringHandler

INFERENCE_COL = 'inference'


def monitor(df: pd.DataFrame, inference: pd.Series, monitoring_handler: MonitoringHandler):
    df[INFERENCE_COL] = inference
    monitoring_handler.save_inference(inference_df=df)
