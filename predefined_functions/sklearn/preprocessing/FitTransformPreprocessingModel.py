import numpy as np
import pandas as pd
from predefined_functions.types.list import list_types


class SklearnPreprocessingModelFitTransform:

    fit_transform = "fit_transform"
    transform = "transform"

    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "LIST": (list_types,),
                "preprocessing_model": ("PREPROCESSING_MODEL",),
                "mode": (["fit_transform", "transform"],),
            },
            "optional": {"COLUMNS": ("STRING",)},
        }

    CATEGORY = "sklearn/preprocessing"

    RETURN_NAMES = (
        "PROPROCESSED DATA",
        "preprocessing model",
    )

    RETURN_TYPES = (
        list_types,
        "PREPROCESSING_MODEL",
    )

    FUNCTION = "ftm"

    def ftm(self, LIST, preprocessing_model, COLUMNS, mode):

        if type(LIST) == np.ndarray:
            if COLUMNS != "":
                columns_idx = [
                    int(i) if i.isnumeric() else i for i in COLUMNS.split(",")
                ]
                if mode == self.fit_transform:
                    LIST[:, columns_idx] = preprocessing_model.fit_transform(
                        LIST[:, columns_idx]
                    )
                else:
                    LIST[:, columns_idx] = preprocessing_model.transform(
                        LIST[:, columns_idx]
                    )
                return (
                    LIST,
                    preprocessing_model,
                )
            if mode == self.fit_transform:
                return (
                    preprocessing_model.fit_transform(LIST),
                    preprocessing_model,
                )
            else:
                return (
                    preprocessing_model.transform(LIST),
                    preprocessing_model,
                )
        elif type(LIST) == pd.DataFrame:
            if COLUMNS != "":
                columns_idx = COLUMNS.split(",")

                if mode == self.fit_transform:

                    try:
                        for i in columns_idx:
                            LIST[i] = preprocessing_model.fit_transform(LIST[i])
                    except:
                        LIST[columns_idx] = preprocessing_model.fit_transform(
                            LIST[columns_idx]
                        )
                else:
                    try:
                        for i in columns_idx:
                            LIST[i] = preprocessing_model.transform(LIST[i])
                    except:
                        LIST[columns_idx] = preprocessing_model.transform(
                            LIST[columns_idx]
                        )

                return (
                    LIST,
                    preprocessing_model,
                )

            if mode == self.fit_transform:
                return (
                    preprocessing_model.fit_transform(LIST),
                    preprocessing_model,
                )
            else:
                return (
                    preprocessing_model.transform(LIST),
                    preprocessing_model,
                )
        elif type(LIST) == pd.Series:
            raise TypeError("PD_SERIES type not support")
