from imblearn.over_sampling import SMOTE


class ImblearnSmote:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "X": ("PD_DATAFRAME",),
                "Y": ("PD_DATAFRAME",),
                "random_state": ("INT", {"defaultVal": 42}),
            }
        }

    CATEGORY = "imblearn/over_sampling"

    RETURN_NAMES = (
        "X_SMOTE",
        "Y_SMOTE",
    )

    RETURN_TYPES = (
        "PD_DATAFRAME",
        "PD_DATAFRAME",
    )

    FUNCTION = "createSMOTE"

    def createSMOTE(self, X, Y, random_state):
        smote = SMOTE(random_state=random_state)

        X_smote, Y_smote = smote.fit_resample(X, Y)

        return (
            X_smote,
            Y_smote,
        )
