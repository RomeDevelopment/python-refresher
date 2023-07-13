import unittest
import physics


class TestPhysics(unittest.TestCase):
    def test_buoyancy_cal(self):
        self.assertEqual(physics.calculate_buoyancy(100, 100), 98100)
        self.assertEqual(physics.calculate_buoyancy(1 / 9.81, 100), 100)
        self.assertNotEqual(physics.calculate_buoyancy(1 / 9.81, 100), 101)

    def test_float_cal(self):
        self.assertEqual(physics.will_it_float(1, 1000), None)
        self.assertNotEqual(physics.will_it_float(1, 1000), True or False)
        self.assertEqual(physics.will_it_float(2, 1000), True)
        self.assertEqual(physics.will_it_float(1, 2000), False)

    def test_pressure_cal(self):
        self.assertEqual(physics.calculate_pressure(1), 9810)
        self.assertNotEqual(physics.calculate_pressure(1), 9809)
        self.assertEqual(physics.calculate_pressure(1 / 9.81), 1000)


if __name__ == "__main__":
    unittest.main()
