import unittest
from predefined_functions.mlxtend.frequent_patterns.apriori import MlxtendApriori
from predefined_functions.mlxtend.frequent_patterns.assosication_rules import (
    MlxtendAssosicationRules,
)
from predefined_functions.mlxtend.preprocessing.TransactionEncoder import (
    MlxtendTransactionEncoder,
)
from predefined_functions.sklearn.preprocessing.FitTransformPreprocessModel import (
    SklearnFitTransformPreprocessModel,
)
import pandas as pd
import numpy as np


class TestMlxtend(unittest.TestCase):
    def test_transaction_encoder(self):
        dataset = [
            ["Milk", "Onion", "Nutmeg", "Kidney Beans", "Eggs", "Yogurt"],
            ["Dill", "Onion", "Nutmeg", "Kidney Beans", "Eggs", "Yogurt"],
            ["Milk", "Apple", "Kidney Beans", "Eggs"],
            ["Milk", "Unicorn", "Corn", "Kidney Beans", "Yogurt"],
            ["Corn", "Onion", "Onion", "Kidney Beans", "Ice cream", "Eggs"],
        ]

        mlxtenTransactionEncoder = MlxtendTransactionEncoder()
        fitTransform = SklearnFitTransformPreprocessModel()

        model = mlxtenTransactionEncoder.createTE()[0]
        res0, res1 = fitTransform.fit_transform_model(dataset, model, "")
        self.assertIsInstance(res0, np.ndarray)

    def test_apiori(self):
        dataset = [
            ["Milk", "Onion", "Nutmeg", "Kidney Beans", "Eggs", "Yogurt"],
            ["Dill", "Onion", "Nutmeg", "Kidney Beans", "Eggs", "Yogurt"],
            ["Milk", "Apple", "Kidney Beans", "Eggs"],
            ["Milk", "Unicorn", "Corn", "Kidney Beans", "Yogurt"],
            ["Corn", "Onion", "Onion", "Kidney Beans", "Ice cream", "Eggs"],
        ]

        mlxtenTransactionEncoder = MlxtendTransactionEncoder()
        fitTransform = SklearnFitTransformPreprocessModel()

        model = mlxtenTransactionEncoder.createTE()[0]
        res0, res1 = fitTransform.fit_transform_model(dataset, model, "")
        self.assertIsInstance(res0, np.ndarray)
        df = pd.DataFrame(res0, columns=model.columns_)

        mlxtendApriori = MlxtendApriori()

        res2 = mlxtendApriori.ap(df, 0.6)[0]

        self.assertIsInstance(res2, pd.DataFrame)
        self.assertListEqual(res2.columns.to_list(), ["support", "itemsets"])

    def test_assosiation_rules(self):
        dataset = [
            ["Milk", "Onion", "Nutmeg", "Kidney Beans", "Eggs", "Yogurt"],
            ["Dill", "Onion", "Nutmeg", "Kidney Beans", "Eggs", "Yogurt"],
            ["Milk", "Apple", "Kidney Beans", "Eggs"],
            ["Milk", "Unicorn", "Corn", "Kidney Beans", "Yogurt"],
            ["Corn", "Onion", "Onion", "Kidney Beans", "Ice cream", "Eggs"],
        ]

        mlxtenTransactionEncoder = MlxtendTransactionEncoder()
        fitTransform = SklearnFitTransformPreprocessModel()

        model = mlxtenTransactionEncoder.createTE()[0]
        res0, res1 = fitTransform.fit_transform_model(dataset, model, "")
        self.assertIsInstance(res0, np.ndarray)
        df = pd.DataFrame(res0, columns=model.columns_)

        mlxtendApriori = MlxtendApriori()

        res2 = mlxtendApriori.ap(df, 0.6)[0]

        self.assertIsInstance(res2, pd.DataFrame)
        self.assertListEqual(res2.columns.to_list(), ["support", "itemsets"])

        mlxtendAssosicationRules = MlxtendAssosicationRules()

        res3 = mlxtendAssosicationRules.ar(res2, 0.2, "confidence")[0]

        self.assertIsInstance(res3, pd.DataFrame)
