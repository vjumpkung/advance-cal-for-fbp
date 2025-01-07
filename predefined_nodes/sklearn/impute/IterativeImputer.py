from sklearn.experimental import enable_iterative_imputer  # Enable experimental mode
from sklearn.impute import IterativeImputer
from sklearn.linear_model import LinearRegression


class SklearnIterativeImputer:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "max_iter": ("INT", {"min": 1, "max": 100, "defaultVal": 1}),
                "initial_strategy": (
                    ["mean", "median", "mode"],
                    {"defaultVal": "median"},
                ),
            }
        }

    CATEGORY = "sklearn/impute"

    RETURN_NAMES = ("preprocessing_model",)

    RETURN_TYPES = ("PREPROCESSING_MODEL",)

    FUNCTION = "crateImputer"

    def crateImputer(self, max_iter, initial_strategy):

        imputer = IterativeImputer(
            estimator=LinearRegression(),
            max_iter=max_iter,
            initial_strategy=initial_strategy,
        )

        return (imputer,)
