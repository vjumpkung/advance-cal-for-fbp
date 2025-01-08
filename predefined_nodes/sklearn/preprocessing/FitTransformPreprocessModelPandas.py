import numpy as np


class SklearnFitTransformPreprocessModelPandas:

    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "DATAFRAME": ("PD_DATAFRAME",),
                "preprocessing_model": ("PREPROCESSING_MODEL",),
            },
            "optional": {"COLUMNS": ("STRING",)},
        }

    CATEGORY = "sklearn/preprocessing"

    RETURN_NAME = (
        "Encoded labels",
        "preprocessing_model",
    )

    RETURN_TYPES = (
        "PD_DATAFRAME",
        "PREPROCESSING_MODEL",
    )

    FUNCTION = "fit_transform_model"

    def fit_transform_model(self, DATAFRAME, preprocessing_model, COLUMNS):

        if COLUMNS != "":
            columns_idx = COLUMNS.split(",")

            try:
                for i in columns_idx:
                    DATAFRAME[i] = preprocessing_model.fit_transform(DATAFRAME[i])
            except:
                DATAFRAME[columns_idx] = preprocessing_model.fit_transform(
                    DATAFRAME[columns_idx]
                )

            return (
                DATAFRAME,
                preprocessing_model,
            )

        return (
            preprocessing_model.fit_transform(DATAFRAME),
            preprocessing_model,
        )
