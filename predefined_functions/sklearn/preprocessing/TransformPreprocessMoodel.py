import numpy as np


class SklearnTransformPreprocessModel:

    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "NDARRAY": ("NDARRAY",),
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
        "NDARRAY",
        "PREPROCESSING_MODEL",
    )

    FUNCTION = "transform_model"

    def transform_model(self, NDARRAY, preprocessing_model, COLUMNS):

        if COLUMNS != "":
            columns_idx = [int(i) if i.isnumeric() else i for i in COLUMNS.split(",")]
            NDARRAY[:, columns_idx] = preprocessing_model.transform(
                NDARRAY[:, columns_idx]
            )
            return (
                NDARRAY,
                preprocessing_model,
            )

        return (
            preprocessing_model.transform(NDARRAY),
            preprocessing_model,
        )
