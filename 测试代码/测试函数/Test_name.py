import unittest
from get_name import get_name

class NamesTest(unittest.TestCase):
    """测试get_name.py"""
    def test_first_last_name(self):
        """能够正确地处理像Tom Peter这样的姓名吗？"""
        name = get_name("tom","peter")
        self.assertEqual(name,"Tom Peter")

    def test_first_last_midddle_name(self):
        """能够正确地处理像Jerry Walter Gates这样的姓名吗？"""
        name = get_name("jerry","gates","walter")
        self.assertEqual(name,"Jerry Walter Gates")

unittest.main()