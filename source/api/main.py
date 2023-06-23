import logging

import pandas as pd
from fastapi import FastAPI

from config.api_server import SERVER_ADRESS
from config.monitoring_config import DB_CONNECTION_STRING
from source.domain.entities.customer_columns import DataSetColumns, Education
from source.domain.usecase.monitor import monitor
from source.domain.usecase.predict_model import predict_model, INFERENCE_COL
from source.domain.usecase.train_model import train_model
from source.infrastructure.database_monitoring_handler import DataBaseMonitoringHandler
from source.infrastructure.file_system_model_handler import FilSystemModelHandler

app = FastAPI(root_path=SERVER_ADRESS)
model_handler = FilSystemModelHandler()
monitoring_handler = DataBaseMonitoringHandler(connection_string=DB_CONNECTION_STRING)


@app.get("/")
def root():
    return {'Message': 'API server working fine, you can get swagger on /docs.'}


@app.get("/health")
def health():
    return {'healthcheck': 'Everything OK!'}


@app.post("/train")
def train():
    performance_train, performance_test = train_model(model_handler=model_handler)
    return {'Train mean_squared_error': performance_train,
            'Test mean_squared_error': performance_test}


@app.get("/predict")
def predict(education: Education, age: int, income: float):
    """

    :param education: Le niveau d'étude de la personne (High School, Bachelor, Master, PhD)
    :param age: age of client
    :param income: income of client
    :return:
    """
    df = pd.DataFrame({DataSetColumns.education: [education], DataSetColumns.age: [age],
                       DataSetColumns.income: [income]})
    inference = predict_model(df=df, model_handler=model_handler)
    monitor(df=df, inference=inference, monitoring_handler=monitoring_handler)
    return inference.loc[0, INFERENCE_COL]


@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    logging.exception(f"Exception {exc} happened on request {request}")
    raise exc
