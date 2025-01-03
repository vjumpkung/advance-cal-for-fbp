import pandas as pd


class PandasCheckDtypes:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "dataframe": ("PD_DATAFRAME",),
                "number": ("BOOLEAN", {"defaultVal": False}),
                "object": ("BOOLEAN", {"defaultVal": False}),
                "datetime": ("BOOLEAN", {"defaultVal": False}),
                "timedelta": ("BOOLEAN", {"defaultVal": False}),
                "category": ("BOOLEAN", {"defaultVal": False}),
                "datetimetz": ("BOOLEAN", {"defaultVal": False}),
            }
        }

    CATEGORY = "pandas"

    RETURN_TYPES = ("PD_DATAFRAME",)

    FUNCTION = "select_dtypes"

    def select_dtypes(
        self,
        dataframe: pd.DataFrame,
        number,
        object,
        datetime,
        timedelta,
        category,
        datetimetz,
    ):
        include_list = []
        if number:
            include_list.append("number")
        if object:
            include_list.append("object")
        if datetime:
            include_list.append("datetime")
        if timedelta:
            include_list.append("timedelta")
        if category:
            include_list.append("category")
        if datetimetz:
            include_list.append("datetimez")
        return (dataframe.select_dtypes(include=include_list),)
