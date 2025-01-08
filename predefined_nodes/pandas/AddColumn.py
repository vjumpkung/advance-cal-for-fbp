import pandas as pd
from predefined_nodes.types.any import any


class PandasAddColumn:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "dataframe": ("PD_DATAFRAME",),
                "newColumnName": ("STRING",),
                "value": (any,),
            }
        }

    CATEGORY = "pandas"

    RETURN_NAMES = ("DATAFRAME",)

    RETURN_TYPES = ("PD_DATAFRAME",)

    FUNCTION = "pandas_add_column"

    def pandas_add_column(self, dataframe: pd.DataFrame, newColumnName: str, value):

        dataframe[newColumnName] = value

        return (dataframe,)
