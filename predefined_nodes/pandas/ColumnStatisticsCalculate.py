import pandas as pd


class PandasColumnStatisticsCalculate:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "dataframe": ("PD_DATAFRAME",),
                "method": (["mean", "median", "mode"],),
                "column": ("STRING",),
            }
        }

    CATEGORY = "pandas"

    RETURN_NAMES = ("VALUE",)

    RETURN_TYPES = ("SCALAR",)

    FUNCTION = "pandas_column_statistics"

    def pandas_column_statistics(self, dataframe: pd.DataFrame, method, column):
        if len(column) > 0:
            match method:
                case "mean":
                    return (dataframe[column.split(",")].mean(),)
                case "median":
                    return (dataframe[column.split(",")].median(),)
                case "mode":
                    return (dataframe[column.split(",")].mode(),)
        else:
            raise KeyError("No column select")
