from sklearn.model_selection import train_test_split

from predefined_functions.types.list import list_types


class SklearnTrainTestSplit:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "X": (list_types,),
                "Y": (list_types,),
                "test_size": ("FLOAT", {"min": 0, "max": 1, "step": 0.01}),
                "random_state": ("INT", {"min": 0}),
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
        list_types,
        list_types,
        list_types,
        list_types,
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
