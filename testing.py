import unittest
import buss_logic as bl


num1 = 20
num2 = 10

class TestCalcMethods(unittest.TestCase):
    
    def setUp(self):
        self.num1 = 20
        self.num2 = 10

    def test_add(self):
        expected = num1 + num2
        actual = bl.added(num1, num2)
        self.assertEqual(expected, actual)

    def test_multi(self):
        expected = num1 * num2
        actual = bl.multip(num1, num2)
        self.assertEqual(expected, actual)

    def test_sub(self):        
        expected = num1 - num2
        actual = bl.subt(num1, num2)
        self.assertEqual(expected, actual)
    
    def test_div(self):
        expected = num1 / num2
        actual = bl.divi(num1, num2)

if __name__ == '__main__':
    unittest.main()