from sklearn.neighbors import KNeighborsClassifier
from predefined_functions.types.list import list_types


class SklearnKNeighborsClassifier:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "X": (list_types,),
                "Y": (list_types,),
                "n_neighbors": ("INT", {"defaultVal": 1, "min": 1, "step": 1}),
            }
        }

    CATEGORY = "sklearn/neighbors"

    RETURN_NAMES = ("model",)

    RETURN_TYPES = ("MODEL",)

    FUNCTION = "createKNeighborsClassifier"

    def createKNeighborsClassifier(self, X, Y, n_neighbors):

        model = KNeighborsClassifier(n_neighbors=n_neighbors)

        model.fit(X, Y)

        return (model,)
