from predefined_functions.imblearn.over_sampling.SMOTE import ImblearnSmote
from collections import Counter
from sklearn.datasets import make_classification
import unittest


class TestImBlearn(unittest.TestCase):
    def test_smote(self):
        imbsmote = ImblearnSmote()

        X, y = make_classification(
            n_classes=2,
            class_sep=2,
            weights=[0.1, 0.9],
            n_informative=3,
            n_redundant=1,
            flip_y=0,
            n_features=20,
            n_clusters_per_class=1,
            n_samples=1000,
            random_state=10,
        )

        self.assertDictEqual(Counter(y), {1: 900, 0: 100})

        X_res, y_res = imbsmote.createSMOTE(X=X, Y=y)

        self.assertDictEqual(Counter(y_res), {1: 900, 0: 900})
