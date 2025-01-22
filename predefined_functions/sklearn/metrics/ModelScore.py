from predefined_functions.types.list import list_types


class SklearnModelScore:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "model": ("MODEL", {"forceInput": True}),
                "X_test": (list_types, {"forceInput": True}),
                "Y_test": (list_types, {"forceInput": True}),
            }
        }

    CATEGORY = "sklearn/metrics"

    RETURN_NAMES = ("SCORE",)

    RETURN_TYPES = ("FLOAT",)

    FUNCTION = "report"

    def report(self, model, X_test, Y_test):
        return (model.score(X_test, Y_test),)
