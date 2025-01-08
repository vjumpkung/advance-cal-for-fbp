from sklearn.tree import DecisionTreeClassifier, export_text
from predefined_nodes.types.any import any


class SklearnDecisionTree:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "X": (any,),
                "Y": (any,),
                "criterion": (["entropy", "gini", "log_loss"], {"defaultVal": "gini"}),
                "max_depth": ("INT", {"defaultVal": 3, "min": 1}),
                "random_state": ("INT", {"defaultVal": 0}),
            }
        }

    CATEGORY = "sklearn/tree"

    RETURN_NAMES = (
        "decision tree model",
        "TREE_PREVIEW",
    )

    RETURN_TYPES = (
        "MODEL",
        "STRING",
    )

    FUNCTION = "dt"

    def dt(self, X, Y, criterion, max_depth, random_state):

        model = DecisionTreeClassifier(
            criterion=criterion, max_depth=max_depth, random_state=random_state
        )

        model.fit(X, Y)

        pt = export_text(model, feature_names=list(X.columns))

        return (
            model,
            pt,
        )
