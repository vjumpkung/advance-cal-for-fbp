import numpy as np
import pandas as pd
from predefined_functions.types.list import list_types


class SklearnLabelEncoderFitTransform:

    fit_transform = "fit_transform"
    transform = "transform"

    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "LIST": (list_types,),
                "label_encoder_model": ("LABEL_ENCODER_MODEL",),
                "mode": (["fit_transform", "transform"],),
            },
            "optional": {"COLUMNS": ("STRING",)},
        }

    CATEGORY = "sklearn/preprocessing"

    RETURN_NAMES = (
        "Encoded labels",
        "label encoder model",
    )

    RETURN_TYPES = (
        list_types,
        "LABEL_ENCODER_MODEL",
    )

    FUNCTION = "fit_transform_model"

    def fit_transform_model(self, LIST, label_encoder_model, COLUMNS, mode):

        if type(LIST) == np.ndarray:

            if COLUMNS != "":
                columns_idx = [
                    int(i) if i.isnumeric() else i for i in COLUMNS.split(",")
                ]
                if mode == self.fit_transform:
                    LIST[:, columns_idx] = label_encoder_model.fit_transform(
                        LIST[:, columns_idx]
                    )
                else:
                    LIST[:, columns_idx] = label_encoder_model.transform(
                        LIST[:, columns_idx]
                    )
                return (
                    LIST,
                    label_encoder_model,
                )
            if mode == self.fit_transform:
                return (
                    label_encoder_model.fit_transform(LIST),
                    label_encoder_model,
                )
            else:
                return (
                    label_encoder_model.transform(LIST),
                    label_encoder_model,
                )
        elif type(LIST) == pd.DataFrame:
            if COLUMNS != "":
                columns_idx = COLUMNS.split(",")

                if mode == self.fit_transform:

                    try:
                        for i in columns_idx:
                            LIST[i] = label_encoder_model.fit_transform(LIST[i])
                    except:
                        LIST[columns_idx] = label_encoder_model.fit_transform(
                            LIST[columns_idx]
                        )
                else:
                    try:
                        for i in columns_idx:
                            LIST[i] = label_encoder_model.transform(LIST[i])
                    except:
                        LIST[columns_idx] = label_encoder_model.transform(
                            LIST[columns_idx]
                        )

                return (
                    LIST,
                    label_encoder_model,
                )

            if mode == self.fit_transform:
                return (
                    label_encoder_model.fit_transform(LIST),
                    label_encoder_model,
                )
            else:
                return (
                    label_encoder_model.transform(LIST),
                    label_encoder_model,
                )
        elif type(LIST) == pd.Series:
            raise TypeError("PD_SERIES type not support")
