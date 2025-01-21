from predefined_functions.types.any import any


class SklearnModelPredict:
    @classmethod
    def INPUT_TYPES(self):
        return {"required": {"model": ("MODEL",), "X_test": (any,)}}

    CATEGORY = "sklearn/predict"

    RETURN_NAMES = ("Y_pred",)

    RETURN_TYPES = ("NDARRAY",)

    FUNCTION = "model_pred"

    def model_pred(self, model, X_test):
        return (model.predict(X_test),)
