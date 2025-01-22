from sklearn.linear_model import LogisticRegression
from predefined_functions.types.list import list_types


class SklearnLogisticRegression:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "X": (list_types,),
                "Y": (list_types,),
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
