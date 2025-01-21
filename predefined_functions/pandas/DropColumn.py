import pandas as pd


class PandasDropColumn:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "dataframe": ("PD_DATAFRAME",),
                "column": ("STRING",),
            }
        }

    CATEGORY = "pandas"

    RETURN_NAMES = ("DATAFRAME",)

    RETURN_TYPES = ("PD_DATAFRAME",)

    FUNCTION = "pandas_drop_columns"

    def pandas_drop_columns(self, dataframe: pd.DataFrame, column: str):
        column_lst = column.split(",")
        df2 = dataframe.drop(column_lst, axis=1)

        return (df2,)
