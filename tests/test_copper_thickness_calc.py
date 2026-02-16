import unittest

from tools.copper_thickness_calc import (
    Measurement,
    meters_to_micrometers,
    micrometers_to_oz,
    resistance_to_20c,
    thickness_from_measurement,
)


class CopperThicknessCalcTests(unittest.TestCase):
    def test_resistance_to_20c_same_temperature(self):
        self.assertAlmostEqual(resistance_to_20c(0.01, 20.0), 0.01)

    def test_resistance_to_20c_higher_temperature(self):
        compensated = resistance_to_20c(0.01039, 30.0)
        self.assertAlmostEqual(compensated, 0.01, places=6)

    def test_thickness_estimation(self):
        # 10cm x 1mm coupon, about 35um copper => ~49.26mΩ at 20°C
        m = Measurement(resistance_ohm=0.04926, length_m=0.1, width_m=0.001, temperature_c=20.0)
        thickness_um = meters_to_micrometers(thickness_from_measurement(m))
        self.assertAlmostEqual(thickness_um, 35.0, delta=0.3)

    def test_oz_conversion(self):
        self.assertAlmostEqual(micrometers_to_oz(34.79), 1.0, places=4)


if __name__ == "__main__":
    unittest.main()
