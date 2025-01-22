class ListTypes(str):

    def __eq__(self, _) -> bool:

        if _ in ["NDARRAY", "PD_DATAFRAME", "PD_SERIES"]:
            return True

        return False

    def __ne__(self, __value: object) -> bool:
        return False


list_types = ListTypes("NDARRAY,PD_DATAFRAME,PD_SERIES")
