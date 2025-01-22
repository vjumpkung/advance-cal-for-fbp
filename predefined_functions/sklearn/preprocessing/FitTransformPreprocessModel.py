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

    RETURN_NAMES = (
        "preprocessed data",
        "preprocessing_model",
    )

    RETURN_TYPES = (
        "NDARRAY",
        "PREPROCESSING_MODEL",
    )

    FUNCTION = "fit_transform_model"

    def fit_transform_model(self, NDARRAY, preprocessing_model, COLUMNS):
        """
        Apply preprocessing model to specified columns in NDARRAY.

        Args:
            NDARRAY: Input numpy array
            preprocessing_model: Sklearn preprocessor (e.g., StandardScaler, MinMaxScaler)
            COLUMNS: Comma-separated string of column indices or empty string for all columns
        """
        if COLUMNS:  # If COLUMNS is not empty
            # Convert column indices from string to int if numeric
            columns_idx = [int(i) if i.isnumeric() else i for i in COLUMNS.split(",")]

            if len(columns_idx) == 1:
                # For single column, reshape to 2D array
                col_idx = columns_idx[0]
                temp = NDARRAY[:, col_idx].reshape(-1, 1)
                NDARRAY[:, col_idx] = preprocessing_model.fit_transform(temp).ravel()
            else:
                # For multiple columns
                temp = NDARRAY[:, columns_idx]
                NDARRAY[:, columns_idx] = preprocessing_model.fit_transform(temp)

            return NDARRAY, preprocessing_model

        # If no columns specified, transform entire array
        return preprocessing_model.fit_transform(NDARRAY), preprocessing_model
