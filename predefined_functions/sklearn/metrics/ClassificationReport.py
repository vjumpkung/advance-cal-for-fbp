from sklearn.metrics import confusion_matrix, classification_report
from predefined_functions.types.list import list_types


class SklearnClassificationReport:
    @classmethod
    def INPUT_TYPES(self):
        return {"required": {"y_true": (list_types,), "y_pred": (list_types,)}}

    CATEGORY = "sklearn/metrics"

    RETURN_NAMES = (
        "report",
        "confusion matrix",
    )

    RETURN_TYPES = (
        "STRING",
        list_types,
    )

    FUNCTION = "get_classification_report"

    def get_classification_report(self, y_true, y_pred):

        cm = confusion_matrix(y_true=y_true, y_pred=y_pred)
        cr = classification_report(y_true=y_true, y_pred=y_pred)

        return (
            cr,
            cm,
        )
