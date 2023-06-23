from enum import Enum

import pandas as pd


class DataSetColumns:
    age = 'age'
    income = 'income'
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
