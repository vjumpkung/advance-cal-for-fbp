from sklearn.preprocessing import LabelEncoder


class SklearnLabelEncoder:
    @classmethod
    def INPUT_TYPES(self):
        return {}

    CATEGORY = "sklearn/preprocessing"

    RETURN_NAMES = ("preprocessing_model",)

    RETURN_TYPES = ("PREPROCESSING_MODEL",)

    FUNCTION = "createLabelEncoder"

    def createLabelEncoder(self):

        le = LabelEncoder()

        return (le,)
