import os.path
from codecarbon import track_emissions
from enum import Enum

import mlflow.sklearn
import pandas as pd
import pandera as pa
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

from data import DATA_PATH
from models import MODEL_REGISTRY
from source.domain.port.model_handler import ModelHandler
from source.domain.entities.customer_data_handler import RawCustomerSchema

MODEL_PATH = os.path.join(MODEL_REGISTRY, 'model.joblib')


class DataSetColumns:
    name = 'name'
    age = 'age'
    education = 'education'
    spending = 'spending'


class Education(str, Enum):
    high_school = 'High School'
    bachelor = 'Bachelor'
    master = 'Master'
    phd = 'PhD'


EDUCATION_LEVEL = pd.DataFrame({
    'education_level': [1, 2, 3, 4],
    DataSetColumns.education: ['High School', 'Bachelor', 'Master', 'PhD']
})


# TODO: [TP3] Retirer decorateur @pa.check_input(RawCustomerSchema)
# TODO: [TP3] Ajouter une verification sur l'input en utilisant les checks définis
# TODO: [TP3] Observer l'erreur, ici le check génère une erreur pour spending > 1
# TODO: [TP3] Utiliser la methode validate pour filtrer les lignes qui ne passent pas les checks et logger ces lignes
@pa.check_input(RawCustomerSchema)
def prepare_data(raw_customer_df: pa.typing.DataFrame[RawCustomerSchema]):
    raw_customer_df = raw_customer_df.merge(EDUCATION_LEVEL, on=DataSetColumns.education).drop(columns=[DataSetColumns.education])
    return raw_customer_df


@track_emissions(project_name='Train model', offline=True, country_iso_code='FRA')
def train_model(model_handler: ModelHandler):
    df = pd.read_csv(os.path.join(DATA_PATH, 'customer_data.csv'), sep=',')
    X_train, X_test, y_train, y_test = train_test_split(df[[DataSetColumns.age, DataSetColumns.education]],
                                                        df[DataSetColumns.spending], test_size=0.33, random_state=42)
    X_train = prepare_data(X_train)
    X_test = prepare_data(X_test)
    model = LinearRegression()
    mlflow.sklearn.autolog()
    model.fit(X_train, y_train)
    model_handler.save_model(model)
    performance_train = evaluate_model(model, X_train, y_train)
    performance_test = evaluate_model(model, X_test, y_test)
    return performance_train, performance_test


def evaluate_model(model, X, y):
    y_predicted = model.predict(X)
    return mean_squared_error(y_predicted, y)
