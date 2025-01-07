import pandas as pd


class PandasMathOperationIntoColumn:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "dataframe": ("PD_DATAFRAME",),
                "column": ("STRING",),
                "operator": (["+", "-", "*", "/", "//", "**", "%"],),
                "value": ("FLOAT",),
            }
        }

    CATEGORY = "pandas"

    RETURN_NAMES = ("DATAFRAME",)

    RETURN_TYPES = ("PD_DATAFRAME",)

    FUNCTION = "col_operation"

    def col_operation(
        self, dataframe: pd.DataFrame, column: str, operator: str, value: float
    ):

        columns = column.split(",")

        for col in columns:
            match operator:
                case "+":
                    dataframe[col] = dataframe[col] + value
                case "-":
                    dataframe[col] = dataframe[col] - value
                case "*":
                    dataframe[col] = dataframe[col] * value
                case "/":
                    dataframe[col] = dataframe[col] / value
                case "//":
                    dataframe[col] = dataframe[col] // value
                case "**":
                    dataframe[col] = dataframe[col] ** value
                case "%":
                    dataframe[col] = dataframe[col] % value
                case _:
                    raise KeyError("Invalid Operator")

        return (dataframe,)
