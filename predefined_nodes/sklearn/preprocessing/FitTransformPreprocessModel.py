import numpy as np


class SklearnFitTransformPreprocessModel:

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

    FUNCTION = "fit_transform_model"

    def fit_transform_model(self, NDARRAY, preprocessing_model, COLUMNS):

        if COLUMNS != "":
            columns_idx = [int(i) if i.isnumeric() else i for i in COLUMNS.split(",")]

            if len(columns_idx) == 1:
                NDARRAY[:, *columns_idx] = preprocessing_model.fit_transform(
                    NDARRAY[:, *columns_idx]
                )
            else:
                NDARRAY[:, columns_idx] = preprocessing_model.fit_transform(
                    NDARRAY[:, columns_idx]
                )
            return (
                NDARRAY,
                preprocessing_model,
            )

        return (
            preprocessing_model.fit_transform(NDARRAY),
            preprocessing_model,
        )
