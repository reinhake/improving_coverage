import unittest
from contrived_func import contrived_func


class TestCase(unittest.TestCase):
    def test1(self):
        self.assertTrue(contrived_func(120))
   

if __name__ == '__main__':
    unittest.main(verbosity=2)
