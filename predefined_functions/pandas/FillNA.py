import pandas as pd
from predefined_functions.types.any import any


class PandasFillNA:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "dataframe": ("PD_DATAFRAME",),
                "value": (any,),
            },
            "optional": {"column": ("STRING",)},
        }

    CATEGORY = "pandas"

    RETURN_NAMES = ("DATAFRAME",)

    RETURN_TYPES = ("PD_DATAFRAME",)

    FUNCTION = "pandas_fill_nan"

    def pandas_fill_nan(self, dataframe: pd.DataFrame, value: str, column=None):
        if column == "":
            dataframe = dataframe.fillna(value=value)
        else:
            dataframe[column.split(",")] = dataframe[column.split(",")].fillna(
                value=value
            )
        return (dataframe,)
