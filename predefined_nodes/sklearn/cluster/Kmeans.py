from sklearn.cluster import KMeans


class SklearnKmeans:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "n_clusters": ("INT", {"defaultVal": 3}),
                "X": ("NDARRAY",),
            },
        }

    CATEGORY = "sklearn/cluster"

    RETURN_NAME = (
        "model",
        "y_pred",
    )

    RETURN_TYPES = (
        "MODEL",
        "NDARRAY",
    )

    FUNCTION = "createKmeans"

    def createKmeans(self, n_clusters, X):
        km = KMeans(n_clusters=n_clusters, init="k-means++")

        p = km.fit_predict(X)

        return (
            km,
            p,
        )
