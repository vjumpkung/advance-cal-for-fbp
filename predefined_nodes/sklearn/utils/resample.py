from sklearn.utils import resample
import pandas as pd


class FixImbalanceClass:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "DATAFRAME": ("PD_DATAFRAME",),
                "method": (["min", "max", "mean"],),
                "class_name": ("STRING",),
            },
        }

    CATEGORY = "sklearn/utils"

    RETURN_NAMES = ("DATAFRAME",)

    RETURN_TYPES = ("PD_DATAFRAME",)

    FUNCTION = "fixImB"

    def fixImB(self, DATAFRAME: pd.DataFrame, method: str, class_name: str):
        sampled_df = pd.DataFrame()

        match method:
            case "min":
                samples = int(DATAFRAME[class_name].value_counts().min())
            case "max":
                samples = int(DATAFRAME[class_name].value_counts().max())
            case "mean":
                samples = int(DATAFRAME[class_name].value_counts().mean())

        for class_label in DATAFRAME[class_name].unique():
            # Extract the data for the current class
            class_df = DATAFRAME[DATAFRAME[class_name] == class_label]

            # Upsample the class data to the maxmimum number of samples among all classes
            sampled_class_df = resample(
                class_df, replace=True, n_samples=samples, random_state=42
            )

            # Append the upsampled class data to the oversampled DataFrame
            sampled_df = pd.concat([sampled_df, sampled_class_df])

        return (sampled_df,)
