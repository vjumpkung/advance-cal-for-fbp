from sklearn.model_selection import train_test_split

from predefined_nodes.types.any import any


class SklearnTrainTestSplit:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "X": (any, {"forceInput": True}),
                "Y": (any, {"forceInput": True}),
                "test_size": ("FLOAT", {"min": 0, "max": 1, "step": 0.01}),
                "random_state": ("INT",),
            }
        }

    CATEGORY = "sklearn/model_selection"

    RETURN_NAMES = (
        "X_train",
        "X_test",
        "Y_train",
        "Y_test",
    )

    RETURN_TYPES = (
        "NDARRAY",
        "NDARRAY",
        "NDARRAY",
        "NDARRAY",
    )

    FUNCTION = "traintestsplit"

    def traintestsplit(self, X, Y, test_size, random_state):

        if test_size == 0:
            return (
                X,
                None,
                Y,
                None,
            )

        X_train, X_test, Y_train, Y_test = train_test_split(
            X, Y, test_size=test_size, random_state=random_state
        )

        return (
            X_train,
            X_test,
            Y_train,
            Y_test,
        )
