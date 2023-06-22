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
        alias=CUSTOMER_NAME_COLUMN_NAME
    )
    age: pa.typing.Series[pa.typing.Int64] = pa.Field(
        alias=CUSTOMER_AGE_COLUMN_NAME
    )
    education: pa.typing.Series[pa.typing.String] = pa.Field(
        alias=CUSTOMER_EDUCATION_COLUMN_NAME
        ,
    )
    income: pa.typing.Series[pa.typing.Int64] = pa.Field(
        alias=CUSTOMER_INCOME_COLUMN_NAME
    )
    country: pa.typing.Series[pa.typing.String] = pa.Field(
        alias=CUSTOMER_COUNTRY_COLUMN_NAME
    )

    # TODO: [TP2] Retirer pour l'exemple du TP
    # TODO: [TP2] Ajouter le type pour spending
    # TODO: [TP2] Ajouter un check pour spending pour vérifier si la valeur est comprise entre 0 et 1
    purchase_frequency: pa.typing.Series[pa.typing.Float64] = pa.Field(
        alias=CUSTOMER_PURCHASE_FREQUENCY_COLUMN_NAME
    )

    spending: pa.typing.Series[pa.typing.Float64] = pa.Field(
        alias=CUSTOMER_SPENDING_COLUMN_NAME
    )

    @pa.check("education", name="is_education_valid")
    def is_education_valid(
        cls, education: pa.typing.Series[pa.typing.String]
    ) -> pa.typing.Series[bool]:
        return education.isin(CUSTOMER_EDUCATION_VALUES)

    @pa.check("purchase_frequency", name="is_purchase_frequency_valid")
    def is_purchase_frequency_valid(
        cls, purchase_frequency: pa.typing.Series[pa.typing.Float64]
    ) -> pa.typing.Series[bool]:
        return purchase_frequency.between(0., 1)

    class Config:
        name = "RawCustomerSchema"
        strict = True
        coerce = True
