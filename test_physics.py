import unittest
import physics
import numpy as np


class TestPhysics(unittest.TestCase):
    def test_buoyancy_calculator(self):
        self.assertEqual(physics.calculate_buoyancy(100, 100), 98100)
        self.assertEqual(physics.calculate_buoyancy(1 / 9.81, 100), 100)
        self.assertNotEqual(physics.calculate_buoyancy(1 / 9.81, 100), 101)

    def test_float_calculator(self):
        self.assertEqual(physics.will_it_float(1, 1000), None)
        self.assertNotEqual(physics.will_it_float(1, 1000), True or False)
        self.assertEqual(physics.will_it_float(2, 1000), True)
        self.assertEqual(physics.will_it_float(1, 2000), False)

    def test_pressure_calculator(self):
        self.assertEqual(physics.calculate_pressure(1), 9810 + 101325)
        self.assertNotEqual(physics.calculate_pressure(1), 9809 + 101325)
        self.assertEqual(physics.calculate_pressure(1 / 9.81), 1000 + 101325)

    def test_acceleration_calculator(self):
        self.assertEqual(physics.calculate_acceleration(100, 10), 10)
        self.assertNotEqual(physics.calculate_acceleration(100, 10), 9)
        # self.assertEqual(physics.calculate_acceleration(10, 0), ValueError)
        self.assertEqual(physics.calculate_acceleration(30000, 10), 3000)

    def test_angular_acceleration_calculator(self):
        self.assertEqual(physics.calculate_angular_acceleration(100, 1), 100)
        self.assertNotEqual(physics.calculate_angular_acceleration(300, 10), 31)
        self.assertEqual(physics.calculate_angular_acceleration(20, 2), 10)

    def test_torque_calculator(self):
        self.assertAlmostEqual(
            physics.calculate_torque(30 * np.pi / 180, 300, 10), 1500
        )
        self.assertNotAlmostEqual(
            physics.calculate_torque(30 * np.pi / 180, 100, 10), 501
        )
        self.assertAlmostEqual(physics.calculate_torque(np.pi, 2000, 2000), 0)


if __name__ == "__main__":
    unittest.main()
