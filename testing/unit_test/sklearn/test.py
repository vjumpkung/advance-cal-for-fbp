import unittest

import numpy as np
import pandas as pd
import scipy
from sklearn.datasets import load_iris
from sklearn.experimental import enable_iterative_imputer

from predefined_functions.sklearn.cluster.Kmeans import KMeans, SklearnKmeans
from predefined_functions.sklearn.compose.ColumnTransformers import (
    SklearnColumnTransformer,
)
from predefined_functions.sklearn.impute.IterativeImputer import (
    IterativeImputer,
    SklearnIterativeImputer,
)
from predefined_functions.sklearn.linear_model.LinearRegression import (
    LinearRegression,
    SklearnLinearRegression,
)
from predefined_functions.sklearn.linear_model.LogisticRegression import (
    LogisticRegression,
    SklearnLogisticRegression,
)
from predefined_functions.sklearn.metrics.ClassificationReport import (
    SklearnClassificationReport,
)
from predefined_functions.sklearn.metrics.ModelScore import SklearnModelScore
from predefined_functions.sklearn.neighbors.KNeighborsClassifier import (
    KNeighborsClassifier,
    SklearnKNeighborsClassifier,
)
from predefined_functions.sklearn.predict.Predict import SklearnModelPredict
from predefined_functions.sklearn.preprocessing.FitTransformPreprocessModel import (
    SklearnFitTransformPreprocessModel,
)
from predefined_functions.sklearn.preprocessing.FitTransformPreprocessModelPandas import (
    SklearnFitTransformPreprocessModelPandas,
)
from predefined_functions.sklearn.preprocessing.LabelEncoder import (
    LabelEncoder,
    SklearnLabelEncoder,
)
from predefined_functions.sklearn.preprocessing.MinMaxScaler import (
    MinMaxScaler,
    SklearnMinMaxScaler,
)
from predefined_functions.sklearn.preprocessing.OneHotEncoder import (
    OneHotEncoder,
    SklearnOneHotEncoder,
)
from predefined_functions.sklearn.preprocessing.StandardScaler import (
    SklearnStandardScaler,
    StandardScaler,
)
from predefined_functions.sklearn.preprocessing.TransformPreprocessModel import (
    SklearnTransformPreprocessModel,
)
from predefined_functions.sklearn.preprocessing.TransformPreprocessModelPandas import (
    SklearnTransformPreprocessModelPandas,
)
from predefined_functions.sklearn.tree.DecisionTree import (
    DecisionTreeClassifier,
    SklearnDecisionTree,
)


class TestSklearnPreprocessingModel(unittest.TestCase):

    sklearn_fit_transform = SklearnFitTransformPreprocessModel()
    sklearn_fit_transform_pandas = SklearnFitTransformPreprocessModelPandas()
    sklearn_transform = SklearnTransformPreprocessModel()
    sklearn_transform_pandas = SklearnTransformPreprocessModelPandas()
    sklearn_label_encoder = SklearnLabelEncoder()
    sklearn_standard_scaler = SklearnStandardScaler()
    sklearn_minmax_scaler = SklearnMinMaxScaler()
    sklearn_onehot_encoder = SklearnOneHotEncoder()
    sklearn_column_transformer = SklearnColumnTransformer()

    def test_fit_transform(self):
        df = pd.DataFrame(
            {
                "number": np.random.randint(1, 100, 10),
                "number2": np.random.randint(101, 200, 10),
            }
        )

        arr = df.to_numpy(dtype=np.float64)

        model = self.sklearn_minmax_scaler.createMinMaxScaler()[0]

        res, m = self.sklearn_fit_transform_pandas.fit_transform_model(
            df, model, "number"
        )

        res2, m2 = self.sklearn_fit_transform.fit_transform_model(arr, model, "0")

        self.assertEqual(m, m2)
        self.assertListEqual(list(res.to_numpy()[:, 1]), list(res2[:, 1]))
        self.assertListEqual(list(res.to_numpy()[:, 0]), list(res2[:, 0]))

    def test_transform(self):
        df = pd.DataFrame(
            {
                "number": np.random.randint(1, 100, 10),
                "number2": np.random.randint(101, 200, 10),
            }
        )

        arr = df.to_numpy(dtype=np.float64)

        original_arr = arr.copy()

        copy_arr = arr.copy()

        model = self.sklearn_minmax_scaler.createMinMaxScaler()[0]

        res, m = self.sklearn_fit_transform.fit_transform_model(arr, model, "0")

        res2, m2 = self.sklearn_transform.transform_model(res, model, "1")

        copy_arr[:, [0]] = model.fit_transform(copy_arr[:, [0]])
        copy_arr[:, [1]] = model.transform(copy_arr[:, [1]])

        self.assertTrue(original_arr.tolist() != res2.tolist())
        self.assertTrue(copy_arr.tolist() == res2.tolist())

        self.assertEqual(m, m2)

    def test_preprocess_model(self):
        model1 = self.sklearn_minmax_scaler.createMinMaxScaler()[0]
        model2 = self.sklearn_label_encoder.createLabelEncoder()[0]
        model3 = self.sklearn_standard_scaler.createStandardScaler()[0]
        model4 = self.sklearn_onehot_encoder.createOneHotEncoder()[0]
        self.assertIsInstance(model1, MinMaxScaler)
        self.assertIsInstance(model2, LabelEncoder)
        self.assertIsInstance(model3, StandardScaler)
        self.assertIsInstance(model4, OneHotEncoder)

    def test_col_transformers(self):
        test = self.sklearn_column_transformer.createColumnTransformers(
            [[1, 2, 3, 4]], "OneHotEncoder"
        )[0]
        self.assertIsInstance(test, np.ndarray | scipy.sparse.spmatrix)


class TestSklearnMachineLearningModel(unittest.TestCase):
    sklearn_linear_regression = SklearnLinearRegression()
    sklearn_logistic_regression = SklearnLogisticRegression()
    sklearn_knn = SklearnKNeighborsClassifier()
    sklearn_kmeans = SklearnKmeans()
    sklearn_dtree = SklearnDecisionTree()
    sklearn_mice = SklearnIterativeImputer()
    sklearn_model_score = SklearnModelScore()
    sklearn_classification_report = SklearnClassificationReport()
    sklearn_predict = SklearnModelPredict()

    def test_ml_models(self):
        X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
        y = np.dot(X, np.array([1, 2])) + 3
        model1 = self.sklearn_linear_regression.createLinearRegressionModel(X, y)[0]
        self.assertIsInstance(model1, LinearRegression)

        X, y = load_iris(return_X_y=True)
        model2 = self.sklearn_logistic_regression.createLogisticRegression(X, y, 42)[0]
        self.assertIsInstance(model2, LogisticRegression)

        X = [[0], [1], [2], [3]]
        y = [0, 0, 1, 1]
        model3 = self.sklearn_knn.createKNeighborsClassifier(X, y, 5)[0]
        self.assertIsInstance(model3, KNeighborsClassifier)

        X = np.array([[1, 2], [1, 4], [1, 0], [10, 2], [10, 4], [10, 0]])
        model4 = self.sklearn_kmeans.createKmeans(2, X)[0]
        self.assertIsInstance(model4, KMeans)

        X, y = load_iris(return_X_y=True)
        model5 = self.sklearn_dtree.dt(X, y)[0]
        self.assertIsInstance(model5, DecisionTreeClassifier)

        model6 = self.sklearn_mice.crateImputer()[0]
        self.assertIsInstance(model6, IterativeImputer)

    def test_classification_report(self):
        y_true = [0, 1, 2, 2, 2]
        y_pred = [0, 0, 2, 2, 1]

        cf, cm = self.sklearn_classification_report.get_classification_report(
            y_true=y_true, y_pred=y_pred
        )

        self.assertIsInstance(cf, str | dict)
        self.assertIsInstance(cm, np.ndarray)

    def test_model_score(self):
        x_train = [[0, 1, 2, 3, 4, 5]]
        x_test = [[0, 1, 2, 3, 3, 5]]
        y_true = [[0, 1, 2, 2, 2]]
        y_pred = [[0, 0, 2, 2, 1]]

        lr = LinearRegression().fit(x_train, y_true)

        score = self.sklearn_model_score.report(lr, x_test, y_pred)[0]

        self.assertIsInstance(score, float)

    def test_predict(self):
        x_train = [[0, 1, 2, 3, 4, 5]]
        x_test = [[0, 1, 2, 3, 3, 5]]
        y_true = [[0, 1, 2, 2, 2]]

        lr = LinearRegression().fit(x_train, y_true)

        real = lr.predict(x_test)
        test = self.sklearn_predict.model_pred(lr, x_test)[0]
        self.assertListEqual(real.tolist(), test.tolist())
