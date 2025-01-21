import unittest

import numpy as np
import pandas as pd
from pandas.testing import assert_frame_equal, assert_series_equal

from predefined_functions.pandas.AddColumn import PandasAddColumn
from predefined_functions.pandas.ColumnStatisticsCalculate import (
    PandasColumnStatisticsCalculate,
)
from predefined_functions.pandas.CombineColumn import PandasCombineColumn
from predefined_functions.pandas.Cut import PandasCut
from predefined_functions.pandas.MathOperationIntoColumn import (
    PandasMathOperationIntoColumn,
)
from predefined_functions.pandas.PandasReadFile import PandasReadFile
from predefined_functions.pandas.RemoveNA import PandasRemoveNA
from predefined_functions.pandas.ToNumeric import PandasToNumeric
from predefined_functions.pandas.ValueCount import PandasValueCounts
from predefined_functions.pandas.SplitColumn import SplitColumn
from predefined_functions.pandas.DropColumn import PandasDropColumn


class TestPandas(unittest.TestCase):

    pd_read_file = PandasReadFile()
    pd_add_col = PandasAddColumn()
    pd_stat = PandasColumnStatisticsCalculate()
    pd_combine_col = PandasCombineColumn()
    pd_value_counts = PandasValueCounts()
    pd_to_numeric = PandasToNumeric()
    pd_drop_na = PandasRemoveNA()
    pd_cut = PandasCut()
    pd_math_value = PandasMathOperationIntoColumn()
    pd_split_col = SplitColumn()
    pd_drop_col = PandasDropColumn()

    def test_read_csv(self):
        res = self.pd_read_file.read_file(
            "./testing/unit_test/pandas/test_file.csv", "CSV"
        )[0]
        self.assertIsInstance(res, pd.DataFrame)

    def test_read_excel(self):
        res = self.pd_read_file.read_file(
            "./testing/unit_test/pandas/test_file.xlsx", "EXCEL"
        )[0]
        self.assertIsInstance(res, pd.DataFrame)

    def test_read_json(self):
        res = self.pd_read_file.read_file(
            "./testing/unit_test/pandas/test_file.json", "JSON"
        )[0]
        self.assertIsInstance(res, pd.DataFrame)

    def test_add_column(self):
        res = self.pd_read_file.read_file(
            "./testing/unit_test/pandas/test_file.csv", "CSV"
        )[0]
        z = pd.Series([7, 8, 8])

        res2 = self.pd_add_col.pandas_add_column(res, "z", z)[0]

        self.assertListEqual(res2.columns.to_list(), ["x", "y", "z"])

    def test_pd_statistics(self):
        res = self.pd_read_file.read_file(
            "./testing/unit_test/pandas/test_file.csv", "CSV"
        )[0]

        z = pd.Series([7, 8, 8])

        res1 = self.pd_add_col.pandas_add_column(res, "z", z)[0]

        res2 = self.pd_stat.pandas_column_statistics(res1, "mean", "x")[0]
        res3 = self.pd_stat.pandas_column_statistics(res1, "median", "y")[0]
        res4 = self.pd_stat.pandas_column_statistics(res1, "mode", "z")[0]

        self.assertEqual(float(res2.iloc[0]), float(res["x".split(",")].mean().iloc[0]))
        self.assertEqual(
            float(res3.iloc[0]), float(res["y".split(",")].median().iloc[0])
        )
        self.assertEqual(float(res4.iloc[0]), float(res["z".split(",")].mode().iloc[0]))

    def test_pd_combine(self):
        f = self.pd_read_file.read_file(
            "./testing/unit_test/pandas/test_file.csv", "CSV"
        )[0]

        for i in ["+", "-", "*", "/", "//", "**", "%"]:
            res = self.pd_combine_col.pandas_combine_column(f, "z", "x", "y", i)[0]

            temp = res.copy(deep=True)

            temp["z"] = eval(f'res["x"]{i}res["y"]')

            assert_frame_equal(res, temp)

            self.assertListEqual(["x", "y", "z"], temp.columns.to_list())
            self.assertListEqual(["x", "y", "z"], res.columns.to_list())

    def test_value_count(self):
        f = self.pd_read_file.read_file(
            "./testing/unit_test/pandas/test_file.csv", "CSV"
        )[0]

        res = self.pd_value_counts.pandas_value_counts(f, "x")[0]

        x = f["x"].value_counts()

        self.assertIsInstance(res, pd.Series)
        assert_series_equal(res, x)

    def test_to_numeric(self):
        s = pd.DataFrame({"TEST": ["apple", "1.0", "2", -3]})

        res = self.pd_to_numeric.pandas_to_numeric(s, "TEST")[0]

        temp = s.copy(deep=True)
        temp["TEST"] = pd.to_numeric(s["TEST"], errors="coerce")

        self.assertIsInstance(res, pd.DataFrame)
        assert_frame_equal(res, temp)

    def test_cut(self):
        df = pd.DataFrame({"number": np.random.randint(1, 100, 10)})
        f = pd.cut(x=df["number"], bins=3, labels=["Low", "Medium", "High"])

        temp = df.copy(deep=True)

        res = self.pd_cut.pandas_cut(temp, "Low,Medium,High", "number")[0]

        self.assertIsInstance(res, pd.Series)
        assert_series_equal(res, f)

    def test_drop_na(self):
        df = pd.DataFrame(
            {
                "name": ["Alfred", "Batman", "Catwoman"],
                "toy": [np.nan, "Batmobile", "Bullwhip"],
                "born": [pd.NaT, pd.Timestamp("1940-04-25"), pd.NaT],
            }
        )
        temp = df.copy(deep=True)
        temp = temp.dropna()

        temp2 = df.copy(deep=True)

        res = self.pd_drop_na.pandas_remove_nan(temp2, "")[0]

        assert_frame_equal(res, temp)

    def test_math_value(self):
        df = pd.DataFrame({"number": np.random.randint(1, 100, 10)})

        for i in ["+", "-", "*", "/", "//", "**", "%"]:
            temp = df.copy(deep=True)
            temp["number"] = eval(f"temp['number']{i}1")
            temp2 = df.copy(deep=True)

            res = self.pd_math_value.col_operation(temp2, "number", i, 1)[0]
            assert_frame_equal(res, temp)

    def test_split_col(self):
        df = pd.DataFrame(
            {
                "number": np.random.randint(1, 100, 10),
                "number2": np.random.randint(101, 200, 10),
            }
        )

        res, res2 = self.pd_split_col.pandas_split_column(df, "number2")

        self.assertIn("number", res.columns.to_list())
        self.assertNotIn("number2", res.columns.to_list())
        self.assertIn("number2", res2.columns.to_list())
        self.assertNotIn("number", res2.columns.to_list())

    def test_drop_col(self):
        df = pd.DataFrame(
            {
                "number": np.random.randint(1, 100, 10),
                "number2": np.random.randint(101, 200, 10),
            }
        )

        res = self.pd_drop_col.pandas_drop_columns(df, "number2")[0]

        self.assertNotIn("number2", res.columns.to_list())
