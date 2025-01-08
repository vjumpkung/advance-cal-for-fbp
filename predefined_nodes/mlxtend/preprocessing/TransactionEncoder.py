from mlxtend.preprocessing import TransactionEncoder


class MlxtendTransactionEncoder:
    @classmethod
    def INPUT_TYPES(self):
        return {}

    CATEGORY = "mlxtend/preprocessing"

    RETURN_NAMES = ("preprocessing_model",)

    RETURN_TYPES = ("PREPROCESSING_MODEL",)

    FUNCTION = "createTE"

    def createTE(self):

        m = TransactionEncoder()

        return (m,)
