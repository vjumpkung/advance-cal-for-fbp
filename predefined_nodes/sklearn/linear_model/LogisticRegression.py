from sklearn.linear_model import LogisticRegression


class SklearnLogisticRegression:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "X": ("NDARRAY",),
                "Y": ("NDARRAY",),
                "random_state": ("INT", {"default": 42}),
            }
        }

    CATEGORY = "sklearn/linear_model"

    RETURN_NAMES = ("model",)

    RETURN_TYPES = ("MODEL",)

    FUNCTION = "createLogisticRegression"

    def createLogisticRegression(self, X, Y, random_state):

        model = LogisticRegression(random_state=random_state)

        model.fit(X, Y)

        return (model,)
