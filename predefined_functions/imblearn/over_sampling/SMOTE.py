from imblearn.over_sampling import SMOTE
from predefined_functions.types.list import list_types


class ImblearnSmote:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "X": (list_types,),
                "Y": (list_types,),
                "random_state": ("INT", {"defaultVal": 42}),
            }
        }

    CATEGORY = "imblearn/over_sampling"

    RETURN_NAMES = (
        "X_SMOTE",
        "Y_SMOTE",
    )

    RETURN_TYPES = (
        list_types,
        list_types,
    )

    FUNCTION = "createSMOTE"

    def createSMOTE(self, X, Y, random_state=42):
        smote = SMOTE(random_state=random_state)

        X_smote, Y_smote = smote.fit_resample(X, Y)

        return (
            X_smote,
            Y_smote,
        )
