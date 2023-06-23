import pandera as pa


class PredictionSchema(pa.DataFrameModel):
    inference: pa.typing.Series[pa.typing.Float64] = pa.Field(
        alias="inference"
    )

    @pa.check("inference", name="is_inference_valid")
    def is_education_valid(
            cls, inference: pa.typing.Series[pa.typing.Float64]
    ) -> pa.typing.Series[bool]:
        return inference.between(0., 100000)
