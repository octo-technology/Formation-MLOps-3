import pandera as pa


CUSTOMER_NAME_COLUMN_NAME = "name"
CUSTOMER_AGE_COLUMN_NAME = "age"
CUSTOMER_EDUCATION_COLUMN_NAME = "education"
CUSTOMER_INCOME_COLUMN_NAME = "income"
CUSTOMER_COUNTRY_COLUMN_NAME = "country"
CUSTOMER_PURCHASE_FREQUENCY_COLUMN_NAME = "purchase_frequency"
CUSTOMER_SPENDING_COLUMN_NAME = "spending"

CUSTOMER_EDUCATION_VALUES = ["High School", "Master", "Bachelor", "PhD"]


class RawCustomerSchema(pa.DataFrameModel):
    name: pa.typing.Series[pa.typing.String] = pa.Field(
        alias=CUSTOMER_NAME_COLUMN_NAME, coerce=True
    )
    age: pa.typing.Series[pa.typing.Int64] = pa.Field(
        alias=CUSTOMER_AGE_COLUMN_NAME, coerce=True, gt=0
    )
    education: pa.typing.Series[pa.typing.String] = pa.Field(
        alias=CUSTOMER_EDUCATION_COLUMN_NAME,
        coerce=True,
        isin=CUSTOMER_EDUCATION_VALUES,
    )
    income: pa.typing.Series[pa.typing.Int64] = pa.Field(
        alias=CUSTOMER_INCOME_COLUMN_NAME, coerce=True
    )
    country: pa.typing.Series[pa.typing.String] = pa.Field(
        alias=CUSTOMER_COUNTRY_COLUMN_NAME, coerce=True
    )
    purchase_frequency: pa.typing.Series[pa.typing.Float64] = pa.Field(
        alias=CUSTOMER_PURCHASE_FREQUENCY_COLUMN_NAME, coerce=True
    )
    # TODO: Retirer pour lexemple du TP
    # TODO: Ajouter le type pour spending préciser le type
    # TODO: Ajouter un check pour avoir une valeur comprise entre 0 et 1
    spending: pa.typing.Series[pa.typing.Float64] = pa.Field(
        alias=CUSTOMER_SPENDING_COLUMN_NAME, coerce=True
    )
