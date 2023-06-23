from datetime import datetime

import pandas as pd
import pytz

from source.domain.port.monitoring_handler import MonitoringHandler

DATETIME_COL = 'datetime'
INFERENCE_COL = 'inference'


def monitor(df: pd.DataFrame, inference: pd.Series, monitoring_handler: MonitoringHandler):
    df[INFERENCE_COL] = inference
    df[DATETIME_COL] = datetime.now().astimezone(pytz.UTC)
    monitoring_handler.save_inference(inference_df=df)
