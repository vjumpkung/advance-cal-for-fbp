from sklearn.metrics import confusion_matrix, classification_report


class SklearnClassificationReport:
    @classmethod
    def INPUT_TYPES(self):
        return {"required": {"y_true": ("NDARRAY",), "y_pred": ("NDARRAY",)}}

    CATEGORY = "sklearn/metrics"

    RETURN_NAMES = (
        "report",
        "confusion matrix",
    )

    RETURN_TYPES = (
        "STRING",
        "NDARRAY",
    )

    FUNCTION = "get_classification_report"

    def get_classification_report(self, y_true, y_pred):

        cm = confusion_matrix(y_true=y_true, y_pred=y_pred)
        cr = classification_report(y_true=y_true, y_pred=y_pred)

        return (
            cr,
            cm,
        )
