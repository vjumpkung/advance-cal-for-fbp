import pandas as pd


class PandasCut:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "dataframe": ("PD_DATAFRAME",),
                "labels": ("STRING", {"defaultVal": "Low,Medium,High"}),
                "column": ("STRING",),
            },
        }

    CATEGORY = "pandas"

    RETURN_NAMES = ("SERIES",)

    RETURN_TYPES = ("PD_SERIES",)

    FUNCTION = "pandas_cut"

    def pandas_cut(self, dataframe: pd.DataFrame, labels: str, column: str):

        lb = labels.split(",")

        opt = pd.cut(dataframe[column], bins=len(lb), labels=lb)

        return (opt,)
