import pandas as pd


class PandasGetDummies:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "dataframe": ("PD_DATAFRAME",),
                "column": ("STRING",),
            },
        }

    CATEGORY = "pandas"

    RETURN_NAMES = ("DATAFRAME",)

    RETURN_TYPES = ("PD_DATAFRAME",)

    FUNCTION = "pandas_get_dummies"

    def pandas_get_dummies(self, dataframe: pd.DataFrame, column: str):
        col = column.split(",")

        dataframe = pd.get_dummies(dataframe, columns=col)

        return (dataframe,)
