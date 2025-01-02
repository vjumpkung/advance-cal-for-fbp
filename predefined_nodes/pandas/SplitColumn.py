import pandas as pd


class SplitColumn:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "dataframe": ("PD_DATAFRAME",),
                "column": ("STRING",),
            }
        }

    CATEGORY = "pandas"

    RETURN_NAMES = (
        "X",
        "Y",
    )

    RETURN_TYPES = (
        "PD_DATAFRAME",
        "PD_SERIES",
    )

    FUNCTION = "pandas_split_column"

    def pandas_split_column(self, dataframe: pd.DataFrame, column: str):
        column_lst = column.split(",")
        df1 = dataframe[column_lst]
        df2 = dataframe.drop(column_lst, axis=1)

        return (
            df2,
            df1,
        )
