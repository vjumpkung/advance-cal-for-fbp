from predefined_nodes.types.any import any


class SklearnModelScore:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "model": ("MODEL", {"forceInput": True}),
                "X_test": (any, {"forceInput": True}),
                "Y_test": (any, {"forceInput": True}),
            }
        }

    CATEGORY = "sklearn/metrics"

    RETURN_NAMES = ("SCORE",)

    RETURN_TYPES = ("FLOAT",)

    FUNCTION = "report"

    def report(self, model, X_test, Y_test):
        return (model.score(X_test, Y_test),)
