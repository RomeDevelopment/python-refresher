import unittest
from bank import bank

mybank = bank(1000, "Rome", 1000)


class TestBank(unittest.TestCase):
    def Test_withdraw(self):
        self.assertEqual(bank.withdraw(mybank, 300), 700)
        self.assertEqual(bank.withdraw(mybank, 200), 800)
        self.assertNotEqual(bank.withdraw(mybank, 100), 899)


if __name__ == "__main__":
    unittest.main()
