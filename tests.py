import unittest
from contrived_func import contrived_func


class TestCase(unittest.TestCase):
    def test1(self):
        self.assertTrue(contrived_func(120))

    def test2(self):
        self.assertFalse(contrived_func(0))

    def test3(self):
        self.assertTrue(contrived_func(150))

    def test4(self):
        self.assertTrue(contrived_func(46))

    def test5(self):
        self.assertFalse(contrived_func(50))

    def test6(self):
        self.assertFalse(contrived_func(6))

    def test7(self):
        self.assertFalse(contrived_func(74))

    def test8(self):
        self.assertFalse(contrived_func(5))


if __name__ == '__main__':
    unittest.main(verbosity=2)
