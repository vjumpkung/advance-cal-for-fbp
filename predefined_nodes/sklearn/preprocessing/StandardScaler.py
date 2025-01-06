from sklearn.preprocessing import StandardScaler


class SklearnStandardScaler:
    @classmethod
    def INPUT_TYPES(self):
        return {}

    CATEGORY = "sklearn/preprocessing"

    RETURN_NAMES = ("preprocessing_model",)

    RETURN_TYPES = ("PREPROCESSING_MODEL",)

    FUNCTION = "createStandardScaler"

    def createStandardScaler(self):

        sc = StandardScaler()

        return (sc,)
