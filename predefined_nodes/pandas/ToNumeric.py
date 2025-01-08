import pandas as pd


class PandasToNumeric:
    @classmethod
    def INPUT_TYPES(self):
        return {"required": {"DATAFRAME": ("PD_DATAFRAME",), "column": ("STRING",)}}

    CATEGORY = "pandas"

    RETURN_NAMES = ("DATAFRAME",)

    RETURN_TYPES = ("PD_DATAFRAME",)

    FUNCTION = "pandas_to_numeric"

    def pandas_to_numeric(self, DATAFRAME: pd.DataFrame, column: str):
        col = column.split(",")

        for i in col:
            DATAFRAME[i] = pd.to_numeric(DATAFRAME[i], errors="coerce")

        return (DATAFRAME,)
