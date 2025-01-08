import pandas as pd


class PandasAsType:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {"dataframe": ("PD_DATAFRAME",), "target_type": (["bool"],)},
            "optional": {"column": ("STRING",)},
        }

    CATEGORY = "pandas"

    RETURN_TYPES = ("PD_DATAFRAME",)

    FUNCTION = "pd_astype"

    def pd_astype(self, dataframe: pd.DataFrame, target_type, column):
        if column == "":
            if target_type == "bool":
                return (dataframe.astype(bool),)
        else:
            col = column.split(",")
            if target_type == "bool":
                dataframe[col] = dataframe[col].astype(bool)
            return (dataframe,)
