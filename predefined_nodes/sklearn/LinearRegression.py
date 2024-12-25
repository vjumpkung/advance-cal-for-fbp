from sklearn.linear_model import LinearRegression


class SklearnLinearRegression:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "X": ("LIST",),
                "Y": ("LIST",),
                "fit_intercept": ("BOOLEAN", {"default": True}),
                "copy_X": ("BOOLEAN", {"default": True}),
                "positive": ("BOOLEAN", {"default": False}),
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
