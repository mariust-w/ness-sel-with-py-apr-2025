import unittest

class Calc:
    def add(self,a,b):
        return a+b

    def mul(self, a, b):
        return a * b


class CalcTest(unittest.TestCase):

    def setUp(self):
        self.calc = Calc()

    def test_add(self):
        self.assertEqual(self.calc.add(10,20),30)

    def test_mul(self):
        self.assertTrue((self.calc.mul(10,20) == 200))

if __name__ == '__main__':
    unittest.main()

