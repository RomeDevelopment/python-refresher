import unittest
import hello
import numpy as np

class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello.hello(), "Hello, world!")

    def test_sin(self):
        self.assertEqual(hello.sin(0), 0)
        self.assertEqual(hello.sin(1), 0.8414709848078965)

    def test_cos(self):
        self.assertEqual(hello.cos(0), 1)
        self.assertEqual(hello.cos(1), 0.5403023058681398)

    def test_tan(self):
        self.assertEqual(hello.tan(0), 0)
        self.assertEqual(hello.tan(1), 1.5574077246549023)

    def test_cot(self):
        self.assertEqual(hello.cot(0), float("inf"))
        self.assertEqual(hello.cot(1), 0.6420926159343306)

    def test_mult(self):
        self.assertEqual(hello.mul(0,1), float(0))
        self.assertEqual(hello.mul(1,2000), 2000)
        self.assertEqual()

    def test_add(self):
        self.assertEqual(hello.add(0,1), float(1))
        self.assertEqual(hello.add(1,2000), 2001)
        self.assertEqual(hello.add(3,.14159),3.14159)

    def test_sub(self):
        self.assertEqual(hello.sub(0,2), float(-2))
        self.assertEqual(hello.sub(1,2000), -1999)
        self.assertEqual(hello.sub(300,299),1)

    def test_div(self):
        self.assertEqual(hello.div(0,1), float(0))
        self.assertEqual(hello.div(1,2), .5)
        self.assertEqual(hello.div(3,4),.75)

    def test_sqrt(self):
        self.assertEqual(hello.sqrt(9), float(3))
        self.assertEqual(hello.sqrt(25), 5)
        self.assertNotEqual(hello.sqrt(18),4)

    def test_power(self):
        self.assertEqual(hello.power(0,1), float(0))
        self.assertEqual(hello.power(1,2000), 1)
        self.assertEqual(hello.power(3,2),9)

    def test_log(self):
        self.assertEqual(hello.log(5), np.log(5))
        self.assertEqual(hello.log(10), np.log(10))
        self.assertNotEqual(hello.log(.1),np.log(.2))

    def test_exp(self):
        self.assertEqual(hello.exp(2), np.exp(2))
        self.assertEqual(hello.exp(2000), np.exp(2000))
        self.assertNotEqual(hello.exp(0),.1)

if __name__ == "__main__":
    unittest.main()
