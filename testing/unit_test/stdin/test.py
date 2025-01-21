from predefined_functions.stdin.ReadFile import ReadFile
import unittest


class TestRealfile(unittest.TestCase):

    read_file = ReadFile()

    def test_read_file(self):
        fp = self.read_file.read_file("./testing/unit_test/stdin/test_file.txt")[0]
        self.assertIsInstance(fp, str)
        self.assertEqual(fp, "FILE!!!")
