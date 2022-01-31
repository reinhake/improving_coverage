import unittest
from contrived_func import contrived_func


class TestCase(unittest.TestCase):
    def test1(self):
        self.assertTrue(contrived_func(120))

    def test2(self):
        self.assertFalse(contrived_func(100))

    def test3(self):
        self.assertFalse(contrived_func(150))

    def test4(self):
        self.assertTrue(contrived_func(46))

    def test5(self):
        self.assertFalse(contrived_func(50))

    def test4(self):
        self.assertFalse(contrived_func(6))


if __name__ == '__main__':
    unittest.main(verbosity=2)
