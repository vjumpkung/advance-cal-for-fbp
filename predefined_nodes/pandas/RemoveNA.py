import pandas as pd
from predefined_nodes.types.any import any


class PandasRemoveNA:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "dataframe": ("PD_DATAFRAME",),
            },
            "optional": {"column": ("STRING",)},
        }

    CATEGORY = "pandas"

    RETURN_NAMES = ("DATAFRAME",)

    RETURN_TYPES = ("PD_DATAFRAME",)

    FUNCTION = "pandas_remove_nan"

    def pandas_remove_nan(self, dataframe: pd.DataFrame, column=None):
        if column == "":
            dataframe = dataframe.dropna()
        else:
            dataframe[column.split(",")] = dataframe[column.split(",")].dropna()
        return (dataframe,)
