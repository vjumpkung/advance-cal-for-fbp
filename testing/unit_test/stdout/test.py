from predefined_functions.stdout.ShowText import ShowText
import unittest


class TestStdout(unittest.TestCase):
    show_text = ShowText()

    def test_show_text(self):
        text = "ABC"
        opt = self.show_text.notify(text)
        self.assertDictEqual({"ui": {"text": (text,)}, "result": (text,)}, opt)
