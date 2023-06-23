import pandas as pd
from sqlalchemy import create_engine

from source.domain.port.monitoring_handler import MonitoringHandler

MONITORING_SELLS_FORECAST = 'monitoring_sells_forecast'


class DataBaseMonitoringHandler(MonitoringHandler):
    def __init__(self, connection_string: str):
        self.connection_string = connection_string

    def save_inference(self, inference_df: pd.DataFrame) -> None:
        engine = create_engine(self.connection_string)
        inference_df.to_sql(MONITORING_SELLS_FORECAST, con=engine, if_exists='append', index=False)
