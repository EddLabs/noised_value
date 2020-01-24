from unittest import TestCase
from lab_value.lab_value import LabValue


class TestLabValue(TestCase):

    def setUp(self):
        self.places = 5

    def check(self):
        self.assertAlmostEqual(self.expected_val, self.v.val, places=self.places,
                               msg="Value is different than expected")
        self.assertAlmostEqual(self.expected_var, self.v.var, places=self.places,
                               msg="Variance is different than expected")
        self.assertAlmostEqual(self.expected_err, self.v.err, places=self.places,
                               msg="Error is different than expected")
        self.assertAlmostEqual(self.expected_relative_err, self.v.relative_err, places=self.places,
                               msg="Relative error is different than expected")

    # Initialization

    def test_init_without_variance_or_error(self):
        self.v = LabValue(val=1.5)
        self.expected_val = 1.5
        self.expected_var = 0
        self.expected_err = 0
        self.expected_relative_err = 0

        self.check()

    def test_init_with_variance(self):
        self.v = LabValue(val=1.5, err=0.5)
        self.expected_val = 1.5
        self.expected_var = 0.25
        self.expected_err = 0.5
        self.expected_relative_err = 0.33333

        self.check()

    def test_init_with_error(self):
        self.v = LabValue(val=1.5, err=0.5)
        self.expected_val = 1.5
        self.expected_var = 0.25
        self.expected_err = 0.5
        self.expected_relative_err = 0.33333

        self.check()

    def test_init_with_both_variance_and_error_raises_value_error(self):
        self.assertRaises(ValueError, LabValue, val=1.5, var=0.25, err=0.5)

    def test_init_with_negative_variance_raises_value_error(self):
        self.assertRaises(ValueError, LabValue, val=1.5, var=-0.25)

    def test_init_with_negative_error_raises_value_error(self):
        self.assertRaises(ValueError, LabValue, val=1.5, err=-0.5)

    # Representation

    def test_representation(self):
        v = LabValue(val=1.5, err=0.5)
        self.assertEqual("1.5 \u00B1 0.5 (33.333% error)", str(v),
                         msg="LabUtil representation is different than expected")

    # Negative

    def test_negative(self):
        self.v = -LabValue(val=1.5, var=0.5)
        self.expected_val = -1.5
        self.expected_var = 0.5
        self.expected_err = 0.70711
        self.expected_relative_err = 0.4714

        self.check()

    # Add

    def test_right_add_constant(self):
        self.v = LabValue(val=1.5, var=0.5) + 2.2
        self.expected_val = 3.7
        self.expected_var = 0.5
        self.expected_err = 0.70711
        self.expected_relative_err = 0.19111

        self.check()

    def test_left_add_constant(self):
        self.v = 2.2 + LabValue(val=1.5, var=0.5)
        self.expected_val = 3.7
        self.expected_var = 0.5
        self.expected_err = 0.70711
        self.expected_relative_err = 0.19111

        self.check()

    def test_add_other_lab_value(self):
        self.v = LabValue(val=1.5, var=0.5) + LabValue(val=2.2, var=2.75)
        self.expected_val = 3.7
        self.expected_var = 3.25
        self.expected_err = 1.802775
        self.expected_relative_err = 0.487236

        self.check()

    # Subtract

    def test_right_subtract_constant(self):
        self.v = LabValue(val=1.5, var=0.5) - 2.2
        self.expected_val = -0.7
        self.expected_var = 0.5
        self.expected_err = 0.70711
        self.expected_relative_err = 1.010157

        self.check()

    def test_left_subtract_constant(self):
        self.v = 2.2 - LabValue(val=1.5, var=0.5)
        self.expected_val = 0.7
        self.expected_var = 0.5
        self.expected_err = 0.70711
        self.expected_relative_err = 1.010157

        self.check()

    def test_subtract_other_lab_value(self):
        self.v = LabValue(val=1.5, var=0.5) - LabValue(val=2.2, var=2.75)
        self.expected_val = -0.7
        self.expected_var = 3.25
        self.expected_err = 1.802775
        self.expected_relative_err = 2.57539

        self.check()

    # Multiply

    def test_right_multiply_positive_constant(self):
        self.v = LabValue(val=1.5, var=0.5) * 1.12
        self.expected_val = 1.68
        self.expected_var = 0.6272
        self.expected_err = 0.79196
        self.expected_relative_err = 0.4714

        self.check()

    def test_right_multiply_negative_constant(self):
        self.v = LabValue(val=1.5, var=0.5) * (-1.12)
        self.expected_val = -1.68
        self.expected_var = 0.6272
        self.expected_err = 0.79196
        self.expected_relative_err = 0.4714

        self.check()

    def test_left_multiply_positive_constant(self):
        self.v = 1.12 * LabValue(val=1.5, var=0.5)
        self.expected_val = 1.68
        self.expected_var = 0.6272
        self.expected_err = 0.79196
        self.expected_relative_err = 0.4714

        self.check()

    def test_left_multiply_negative_constant(self):
        self.v = -1.12 * LabValue(val=1.5, var=0.5)
        self.expected_val = -1.68
        self.expected_var = 0.6272
        self.expected_err = 0.79196
        self.expected_relative_err = 0.4714

        self.check()

    def test_multiply_other_positive_lab_value(self):
        self.v = LabValue(val=1.5, var=0.5) * LabValue(val=2.3, var=2.75)
        self.expected_val = 3.45
        self.expected_var = 8.8325
        self.expected_err = 2.97195
        self.expected_relative_err = 0.861435

        self.check()

    def test_multiply_other_negative_lab_value(self):
        self.v = LabValue(val=1.5, var=0.5) * LabValue(val=-2.3, var=2.75)
        self.expected_val = -3.45
        self.expected_var = 8.8325
        self.expected_err = 2.97195
        self.expected_relative_err = 0.861435

        self.check()

    # Division

    def test_right_divide_positive_constant(self):
        self.v = LabValue(val=1.5, var=0.5) / 1.12
        self.expected_val = 1.339285
        self.expected_var = 0.3986
        self.expected_err = 0.631345
        self.expected_relative_err = 0.4714

        self.check()

    def test_right_divide_negative_constant(self):
        self.v = LabValue(val=1.5, var=0.5) / (-1.12)
        self.expected_val = -1.339285
        self.expected_var = 0.3986
        self.expected_err = 0.631345
        self.expected_relative_err = 0.4714

        self.check()

    def test_left_divide_positive_constant(self):
        self.v = 1.12 / LabValue(val=1.5, var=0.5)
        self.expected_val = 0.746666
        self.expected_var = 0.12389
        self.expected_err = 0.35198
        self.expected_relative_err = 0.4714

        self.check()

    def test_divide_other_lab_value(self):
        self.v = LabValue(val=1.5, var=0.5) / LabValue(val=1.12, var=0.2)
        self.expected_val = 1.339285
        self.expected_var = 0.68458
        self.expected_err = 0.82739
        self.expected_relative_err = 0.617787

        self.check()

    # Power

    def test_1st_power(self):
        self.v = LabValue(val=1.5, err=0.5) ** 1
        self.expected_val = 1.5
        self.expected_var = 0.25
        self.expected_err = 0.5
        self.expected_relative_err = 0.33333

        self.check()

    def test_2nd_power(self):
        self.v = LabValue(val=1.5, err=0.5) ** 2
        self.expected_val = 2.25
        self.expected_var = 2.25
        self.expected_err = 1.5
        self.expected_relative_err = 0.666666

        self.check()

    def test_3rd_power(self):
        self.v = LabValue(val=1.5, err=0.5) ** 3
        self.expected_val = 3.375
        self.expected_var = 11.390625
        self.expected_err = 3.375
        self.expected_relative_err = 1

        self.check()

    def test_0_power(self):
        self.v = LabValue(val=1.5, err=0.5) ** 0
        self.expected_val = 1
        self.expected_var = 0
        self.expected_err = 0
        self.expected_relative_err = 0

        self.check()

    def test_negative_power(self):
        self.v = LabValue(val=1.5, err=0.5) ** -1
        self.expected_val = 0.666666
        self.expected_var = 0.049382
        self.expected_err = 0.222222
        self.expected_relative_err = 0.333333

        self.check()

    # N sigma

    def test_n_sigma(self):
        a = LabValue(val=12.62, var=0.36)
        b = LabValue(val=12.5, var=1.44)
        expected_n_sigma = 0.08944
        self.assertAlmostEqual(expected_n_sigma, a.n_sigma(b), places=self.places,
                               msg="N sigma is different than expected")

    def test_inverse_n_sigma_calculation(self):
        a = LabValue(val=12.62, var=0.36)
        b = LabValue(val=12.5, var=1.44)
        expected_n_sigma = 0.08944
        self.assertAlmostEqual(expected_n_sigma, b.n_sigma(a), places=self.places,
                               msg="N sigma is different than expected")
