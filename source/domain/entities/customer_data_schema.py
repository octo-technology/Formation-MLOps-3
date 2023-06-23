import pandera as pa

from source.domain.entities.customer_columns import DataSetColumns, EDUCATION_LEVEL


class RawCustomerSchema(pa.DataFrameModel):
    age: pa.typing.Series[pa.typing.Int64] = pa.Field(
        alias=DataSetColumns.age
    )
    education: pa.typing.Series[pa.typing.String] = pa.Field(
        alias=DataSetColumns.education
    )

    @pa.check("education", name="is_education_valid")
    def is_education_valid(
            cls, education: pa.typing.Series[pa.typing.String]
    ) -> pa.typing.Series[bool]:
        return education.isin(EDUCATION_LEVEL[DataSetColumns.education])

    class Config:
        name = "RawCustomerSchema"
        strict = True
        coerce = True
