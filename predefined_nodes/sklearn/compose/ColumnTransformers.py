import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer


class SklearnColumnTransformer:
    @classmethod
    def INPUT_TYPES(
        self,
    ):
        return {
            "required": {
                "X": ("NDARRAY",),
                "transformers": (["OneHotEncoder"],),
            }
        }

    CATEGORY = "sklearn/compose"

    RETURN_NAMES = ("NDARRAY",)

    RETURN_TYPES = ("NDARRAY",)

    FUNCTION = "createColumnTransformers"

    def createColumnTransformers(self, X, transformers):

        if transformers == "OneHotEncoder":
            ct = ColumnTransformer(
                transformers=[("encoder", OneHotEncoder(), [0])],
                remainder="passthrough",
            )

        return (ct.fit_transform(X),)
