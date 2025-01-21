import unittest

from predefined_functions.types_conversion.AnyToNpArray import AnyToNumPyArray
from predefined_functions.types_conversion.AnyToString import ConvertAnyToString
from predefined_functions.types_conversion.FloatToString import ConvertFloatToString
import pandas as pd
import numpy as np


class TestTypesConvertsion(unittest.TestCase):
    any_to_ndarray = AnyToNumPyArray()
    any_to_str = ConvertAnyToString()
    float_to_str = ConvertFloatToString()

    def test_conversion_to_np(self):
        a = [1, 2, 3]
        b = pd.Series([1, 2, 3])
        c = pd.DataFrame({"x": [1, 2, 3]})

        a_converted = self.any_to_ndarray.convert_to_list(a)[0]
        b_converted = self.any_to_ndarray.convert_to_list(b)[0]
        c_converted = self.any_to_ndarray.convert_to_list(c)[0]

        self.assertIsInstance(a_converted, np.ndarray)
        self.assertIsInstance(b_converted, np.ndarray)
        self.assertIsInstance(c_converted, np.ndarray)

    def test_float_to_string(self):
        a = 1.0
        a_converted = str(a)
        a_res = self.float_to_str.convert_to_string(a)[0]
        self.assertEqual(a_converted, a_res)
        self.assertIsInstance(a_res, str)

    def test_any_to_string(self):
        a = np.array([1, "432424234", 6453252465, "test"])
        a_converted = str(a)
        a_res = self.any_to_str.convert_to_string(a)[0]
        self.assertEqual(a_converted, a_res)
        self.assertIsInstance(a_res, str)
