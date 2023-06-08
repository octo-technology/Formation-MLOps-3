import pandas as pd
from fastapi import FastAPI

from source.domain.train_model import train_model, Education, predict_model, DataSetColumns

app = FastAPI()


@app.get("/health")
def health():
    return {'healthcheck': 'Everything OK!'}


@app.post("/train")
def train():
    performance_train, performance_test = train_model()
    return {'Train mean_squared_error': performance_train,
            'Test mean_squared_error': performance_test}


@app.get("/predict")
def predict(education: Education, age: int):
    """

    :param education: Le niveau d'étude de la personne (High School, Engineer, Bachelor, Master, PhD)
    :param age:
    :return:
    """
    return predict_model(pd.DataFrame({DataSetColumns.education: [education],
                                       DataSetColumns.age: [age]}))[0]
