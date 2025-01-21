import unittest

from predefined_functions.string.StringConcat import StringConcatNode
from predefined_functions.string.StringInput import TextInputNode


class TestString(unittest.TestCase):
    str_concat = StringConcatNode()
    str_input = TextInputNode()

    def test_string(self):
        a = "test"
        res = self.str_input.execute(a)[0]
        self.assertEqual(a, res)

    def test_string_concat(self):
        a = "1"
        b = "1"
        res = self.str_concat.concat_string(a, b)[0]
        self.assertEqual(res, a + b)
