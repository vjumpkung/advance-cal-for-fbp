from sklearn.linear_model import LinearRegression
from predefined_functions.types.list import list_types


class SklearnLinearRegression:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "X": (list_types,),
                "Y": (list_types,),
                "fit_intercept": ("BOOLEAN", {"defaultVal": True}),
                "copy_X": ("BOOLEAN", {"defaultVal": True}),
                "positive": ("BOOLEAN", {"defaultVal": False}),
            }
        }

    CATEGORY = "sklearn/linear_model"

    RETURN_NAMES = ("model",)

    RETURN_TYPES = ("MODEL",)

    FUNCTION = "createLinearRegressionModel"

    def createLinearRegressionModel(
        self, X, Y, fit_intercept=True, copy_X=True, positive=False
    ):

        model = LinearRegression(
            fit_intercept=fit_intercept,
            copy_X=copy_X,
            n_jobs=None,
            positive=positive,
        )

        model.fit(X, Y)

        return (model,)
