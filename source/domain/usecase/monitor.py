from datetime import datetime, timezone

import pandas as pd

from source.domain.port.monitoring_handler import MonitoringHandler

DATETIME_COL = 'datetime'


def monitor(df: pd.DataFrame, inference: pd.DataFrame, monitoring_handler: MonitoringHandler):
    df = pd.concat([df, inference], axis=1)
    df[DATETIME_COL] = datetime.now(timezone.utc)
    monitoring_handler.save_inference(inference_df=df)
