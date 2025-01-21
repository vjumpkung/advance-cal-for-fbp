import pandas as pd


class PandasValueCounts:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "dataframe": ("PD_DATAFRAME",),
                "column": ("STRING",),
            }
        }

    CATEGORY = "pandas"

    RETURN_TYPES = ("PD_SERIES",)

    FUNCTION = "pandas_value_counts"

    def pandas_value_counts(self, dataframe: pd.DataFrame, column: str):
        return (dataframe[column].value_counts(),)
