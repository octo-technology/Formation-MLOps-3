import pandera as pa

from source.domain.entities.customer_columns import DataSetColumns, EDUCATION_LEVEL

CUSTOMER_EDUCATION_VALUES = ["High School", "Master", "Bachelor", "PhD"]


class RawCustomerSchema(pa.DataFrameModel):
    age: pa.typing.Series[pa.typing.Int64] = pa.Field(
        alias=DataSetColumns.age
    )
    education: pa.typing.Series[pa.typing.String] = pa.Field(
        alias=DataSetColumns.education
        ,
    )
    income: pa.typing.Series[pa.typing.Int64] = pa.Field(
        alias=DataSetColumns.income
    )

    @pa.check("education", name="is_education_valid")
    def is_education_valid(
            cls, education: pa.typing.Series[pa.typing.String]
    ) -> pa.typing.Series[bool]:
        return education.isin(EDUCATION_LEVEL[DataSetColumns.education])

    @pa.check("income", name="is_income_valid")
    def is_income_valid(
            cls, purchase_frequency: pa.typing.Series[pa.typing.Float64]
    ) -> pa.typing.Series[bool]:
        return purchase_frequency.between(0., 100000)

    class Config:
        name = "RawCustomerSchema"
        strict = True
        coerce = True
