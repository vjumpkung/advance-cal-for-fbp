from sklearn.preprocessing import MinMaxScaler


class SklearnMinMaxScaler:
    @classmethod
    def INPUT_TYPES(self):
        return {}

    CATEGORY = "sklearn/preprocessing"

    RETURN_NAMES = ("preprocessing_model",)

    RETURN_TYPES = ("PREPROCESSING_MODEL",)

    FUNCTION = "createMinMaxScaler"

    def createMinMaxScaler(self):

        sc = MinMaxScaler()

        return (sc,)
