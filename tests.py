import unittest
from contrived_func import contrived_func


class TestCase(unittest.TestCase):
    # Testing the first if statment to verify that it returns true
    # when val is between 100 and 150
    def test1(self):
        self.assertTrue(contrived_func(120))

    # Testing the first conditional to see if it returns false when
    # the first parameter is false but the second is true
    # that is: 151 < 150 and 151 > 100
    def test2(self):
        self.assertFalse(contrived_func(151))

    # Testing the second conditional to see if it returns true when
    # both parameters are met
    # that is: 260 < 361 and 23 < 24
    def test3(self):
        self.assertTrue(contrived_func(46))

    # Testing the second conditional fails when only one parameter is met
    # however it is satisfied by the third conditional
    # that is: 250 < 361 and 25 < 24
    def test4(self):
        self.assertTrue(contrived_func(50))

    # Testing the nested condition in the second conditional
    # that is: does 6 return false
    def test5(self):
        self.assertFalse(contrived_func(6))

    # Testing the third conditional to see if it returns false when
    # the first conditional returns true but the second is false
    # that is: 9 < 10 and 5476 % 5 == 0
    def test6(self):
        self.assertFalse(contrived_func(74))

    # Testing the third and first conditional to see if the first is
    # not satisfied but the third is
    # First: 150 is not less than 150
    # Third: 150 > 75 and 22500 % 5 == 0
    def test7(self):
        self.assertTrue(contrived_func(150))


if __name__ == '__main__':
    unittest.main(verbosity=2)
