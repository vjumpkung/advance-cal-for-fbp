from sklearn.preprocessing import OneHotEncoder


class SklearnOneHotEncoder:
    @classmethod
    def INPUT_TYPES(self):
        return {}

    CATEGORY = "sklearn/preprocessing"

    RETURN_NAMES = ("preprocessing_model",)

    RETURN_TYPES = ("PREPROCESSING_MODEL",)

    FUNCTION = "createOneHotEncoder"

    def createOneHotEncoder(self):

        oe = OneHotEncoder()

        return (oe,)
