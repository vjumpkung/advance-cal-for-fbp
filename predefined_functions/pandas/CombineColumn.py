import pandas as pd


class PandasCombineColumn:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "dataframe": ("PD_DATAFRAME",),
                "newColumnName": ("STRING",),
                "column_1": ("STRING",),
                "column_2": ("STRING",),
                "operator": (["+", "-", "*", "/", "//", "**", "%"],),
            }
        }

    CATEGORY = "pandas"

    RETURN_NAMES = ("DATAFRAME",)

    RETURN_TYPES = ("PD_DATAFRAME",)

    FUNCTION = "pandas_combine_column"

    def pandas_combine_column(
        self,
        dataframe: pd.DataFrame,
        newColumnName: str,
        column_1: str,
        column_2: str,
        operator: str,
    ):

        match operator:
            case "+":
                dataframe[newColumnName] = dataframe[column_1] + dataframe[column_2]
            case "-":
                dataframe[newColumnName] = dataframe[column_1] - dataframe[column_2]
            case "*":
                dataframe[newColumnName] = dataframe[column_1] * dataframe[column_2]
            case "/":
                dataframe[newColumnName] = dataframe[column_1] / dataframe[column_2]
            case "//":
                dataframe[newColumnName] = dataframe[column_1] // dataframe[column_2]
            case "**":
                dataframe[newColumnName] = dataframe[column_1] ** dataframe[column_2]
            case "%":
                dataframe[newColumnName] = dataframe[column_1] % dataframe[column_2]
            case _:
                raise KeyError("Invalid Operator")

        return (dataframe,)
