import pandera as pa


class PredictionSchema(pa.DataFrameModel):
    inference: pa.typing.Series[pa.typing.Float64] = pa.Field(
        alias="inference"
    )
