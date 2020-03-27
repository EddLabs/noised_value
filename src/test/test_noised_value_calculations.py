from unittest import TestCase

from noised_value.noised_value import NoisedValue, mean, zero, one
from test.base_test_cases import NoisedValueBaseTestCase


class TestNoisedValueInitializationWithoutVarianceOrError(
    TestCase, NoisedValueBaseTestCase
):
    v = NoisedValue(val=1.5)
    expected_val = 1.5
    expected_var = 0
    expected_err = 0
    expected_relative_err = 0


class TestNoisedValueInitializationWithVariance(TestCase, NoisedValueBaseTestCase):
    v = NoisedValue(val=1.5, err=0.5)
    expected_val = 1.5
    expected_var = 0.25
    expected_err = 0.5
    expected_relative_err = 0.33333


class TestNoisedValueInitializationWithError(TestCase, NoisedValueBaseTestCase):
    v = NoisedValue(val=1.5, err=0.5)
    expected_val = 1.5
    expected_var = 0.25
    expected_err = 0.5
    expected_relative_err = 0.33333


class TestNoisedValueInitializationWithValueZero(TestCase, NoisedValueBaseTestCase):
    v = NoisedValue(val=0, err=0.5)
    expected_val = 0
    expected_var = 0.25
    expected_err = 0.5
    expected_relative_err = None


class TestNoisedValueInitializationRaiseError(TestCase):
    def test_init_with_both_variance_and_error_raises_value_error(self):
        self.assertRaises(ValueError, NoisedValue, val=1.5, var=0.25, err=0.5)

    def test_init_with_negative_variance_raises_value_error(self):
        self.assertRaises(ValueError, NoisedValue, val=1.5, var=-0.25)

    def test_init_with_negative_error_raises_value_error(self):
        self.assertRaises(ValueError, NoisedValue, val=1.5, err=-0.5)


class TestNoisedValueRepresentation(TestCase):
    def test_representation_of_zero_value(self):
        v = NoisedValue(val=0, err=0.5)
        self.assertEqual(
            "0 \u00B1 0.5 (\u221E% error)",
            str(v),
            msg="NoisedValue representation is different than expected",
        )

    def test_representation_of_zero_error(self):
        v = NoisedValue(val=1.5)
        self.assertEqual(
            "1.5 \u00B1 0 (0.000% error)",
            str(v),
            msg="NoisedValue representation is different than expected",
        )

    def test_representation_of_non_zero(self):
        v = NoisedValue(val=1.5, err=0.5)
        self.assertEqual(
            "1.5 \u00B1 0.5 (33.333% error)",
            str(v),
            msg="NoisedValue representation is different than expected",
        )


class TestNoisedValueZero(TestCase, NoisedValueBaseTestCase):
    v = zero()
    expected_val = 0
    expected_var = 0
    expected_err = 0
    expected_relative_err = None


class TestNoisedValueOne(TestCase, NoisedValueBaseTestCase):
    v = one()
    expected_val = 1
    expected_var = 0
    expected_err = 0
    expected_relative_err = 0


class TestNoisedValueNegativeValue(TestCase, NoisedValueBaseTestCase):
    v = -NoisedValue(val=1.5, var=0.5)
    expected_val = -1.5
    expected_var = 0.5
    expected_err = 0.70711
    expected_relative_err = 0.4714


class TestNoisedValueRightConstantAddition(TestCase, NoisedValueBaseTestCase):
    v = NoisedValue(val=1.5, var=0.5) + 2.2
    expected_val = 3.7
    expected_var = 0.5
    expected_err = 0.70711
    expected_relative_err = 0.19111


class TestNoisedValueLeftConstantAddition(TestCase, NoisedValueBaseTestCase):
    v = 2.2 + NoisedValue(val=1.5, var=0.5)
    expected_val = 3.7
    expected_var = 0.5
    expected_err = 0.70711
    expected_relative_err = 0.19111


class TestNoisedValueAdditionWithOtherNoisedValue(TestCase, NoisedValueBaseTestCase):
    v = NoisedValue(val=1.5, var=0.5) + NoisedValue(val=2.2, var=2.75)
    expected_val = 3.7
    expected_var = 3.25
    expected_err = 1.802775
    expected_relative_err = 0.487236


class TestNoisedValueRightConstantSubtraction(TestCase, NoisedValueBaseTestCase):
    v = NoisedValue(val=1.5, var=0.5) - 2.2
    expected_val = -0.7
    expected_var = 0.5
    expected_err = 0.70711
    expected_relative_err = 1.010157


class TestNoisedValueLeftConstantSubtraction(TestCase, NoisedValueBaseTestCase):
    v = 2.2 - NoisedValue(val=1.5, var=0.5)
    expected_val = 0.7
    expected_var = 0.5
    expected_err = 0.70711
    expected_relative_err = 1.010157


class TestNoisedValueSubtractionWithOtherNoisedValue(TestCase, NoisedValueBaseTestCase):
    v = NoisedValue(val=1.5, var=0.5) - NoisedValue(val=2.2, var=2.75)
    expected_val = -0.7
    expected_var = 3.25
    expected_err = 1.802775
    expected_relative_err = 2.57539


class TestNoisedValueRightMultiplicationWithPositiveConstant(
    TestCase, NoisedValueBaseTestCase
):
    v = NoisedValue(val=1.5, var=0.5) * 1.12
    expected_val = 1.68
    expected_var = 0.6272
    expected_err = 0.79196
    expected_relative_err = 0.4714


class TestNoisedValueRightMultiplicationWithNegativeConstant(
    TestCase, NoisedValueBaseTestCase
):
    v = NoisedValue(val=1.5, var=0.5) * (-1.12)
    expected_val = -1.68
    expected_var = 0.6272
    expected_err = 0.79196
    expected_relative_err = 0.4714


class TestNoisedValueLeftMultiplicationWithPositiveConstant(
    TestCase, NoisedValueBaseTestCase
):
    v = 1.12 * NoisedValue(val=1.5, var=0.5)
    expected_val = 1.68
    expected_var = 0.6272
    expected_err = 0.79196
    expected_relative_err = 0.4714


class TestNoisedValueLeftMultiplicationWithNegativeConstant(
    TestCase, NoisedValueBaseTestCase
):
    v = -1.12 * NoisedValue(val=1.5, var=0.5)
    expected_val = -1.68
    expected_var = 0.6272
    expected_err = 0.79196
    expected_relative_err = 0.4714


class TestNoisedValueMultiplicationWithOtherPositiveNoisedValue(
    TestCase, NoisedValueBaseTestCase
):
    v = NoisedValue(val=1.5, var=0.5) * NoisedValue(val=2.3, var=2.75)
    expected_val = 3.45
    expected_var = 8.8325
    expected_err = 2.97195
    expected_relative_err = 0.861435


class TestNoisedValueMultiplicationWithOtherNegativeNoisedValue(
    TestCase, NoisedValueBaseTestCase
):
    v = NoisedValue(val=1.5, var=0.5) * NoisedValue(val=-2.3, var=2.75)
    expected_val = -3.45
    expected_var = 8.8325
    expected_err = 2.97195
    expected_relative_err = 0.861435


class TestNoisedValueRightDivisionWithPositiveConstant(
    TestCase, NoisedValueBaseTestCase
):
    v = NoisedValue(val=1.5, var=0.5) / 1.12
    expected_val = 1.339285
    expected_var = 0.3986
    expected_err = 0.631345
    expected_relative_err = 0.4714


class TestNoisedValueRightDivisionWithNegativeConstant(
    TestCase, NoisedValueBaseTestCase
):
    v = NoisedValue(val=1.5, var=0.5) / (-1.12)
    expected_val = -1.339285
    expected_var = 0.3986
    expected_err = 0.631345
    expected_relative_err = 0.4714


class TestNoisedValueLeftDivisionWithPositiveConstant(
    TestCase, NoisedValueBaseTestCase
):
    v = 1.12 / NoisedValue(val=1.5, var=0.5)
    expected_val = 0.746666
    expected_var = 0.12389
    expected_err = 0.35198
    expected_relative_err = 0.4714


class TestNoisedValueLeftDivisionWithNegativeConstant(
    TestCase, NoisedValueBaseTestCase
):
    v = -1.12 / NoisedValue(val=1.5, var=0.5)
    expected_val = -0.746666
    expected_var = 0.12389
    expected_err = 0.35198
    expected_relative_err = 0.4714


class TestNoisedValueDivisionWithOtherPositiveNoisedValue(
    TestCase, NoisedValueBaseTestCase
):
    v = NoisedValue(val=1.5, var=0.5) / NoisedValue(val=1.12, var=0.2)
    expected_val = 1.339285
    expected_var = 0.68458
    expected_err = 0.82739
    expected_relative_err = 0.617787


class TestNoisedValueInteger1Power(TestCase, NoisedValueBaseTestCase):
    v = NoisedValue(val=1.5, err=0.5) ** 1
    expected_val = 1.5
    expected_var = 0.25
    expected_err = 0.5
    expected_relative_err = 0.33333


class TestNoisedValueInteger2Power(TestCase, NoisedValueBaseTestCase):
    v = NoisedValue(val=1.5, err=0.5) ** 2
    expected_val = 2.25
    expected_var = 2.25
    expected_err = 1.5
    expected_relative_err = 0.666666


class TestNoisedValueInteger3Power(TestCase, NoisedValueBaseTestCase):
    v = NoisedValue(val=1.5, err=0.5) ** 3
    expected_val = 3.375
    expected_var = 11.390625
    expected_err = 3.375
    expected_relative_err = 1


class TestNoisedValueInteger0Power(TestCase, NoisedValueBaseTestCase):
    v = NoisedValue(val=1.5, err=0.5) ** 0
    expected_val = 1
    expected_var = 0
    expected_err = 0
    expected_relative_err = 0


class TestNoisedValueIntegerNegativePower(TestCase, NoisedValueBaseTestCase):
    v = NoisedValue(val=1.5, err=0.5) ** -1
    expected_val = 0.666666
    expected_var = 0.049382
    expected_err = 0.222222
    expected_relative_err = 0.333333


class TestNoisedValueSumOfOneValue(TestCase, NoisedValueBaseTestCase):
    v = sum([NoisedValue(val=1.5, err=0.5)])
    expected_val = 1.5
    expected_var = 0.25
    expected_err = 0.5
    expected_relative_err = 0.33333


class TestNoisedValueSumOfTwoValues(TestCase, NoisedValueBaseTestCase):
    v = sum([NoisedValue(val=1.5, err=0.5), NoisedValue(val=0.9, err=0.1)])
    expected_val = 2.4
    expected_var = 0.26
    expected_err = 0.5099
    expected_relative_err = 0.21246


class TestNoisedValueSumOfThreeValues(TestCase, NoisedValueBaseTestCase):
    v = sum(
        [
            NoisedValue(val=1.5, err=0.5),
            NoisedValue(val=0.9, err=0.1),
            NoisedValue(val=1.2, err=0.3),
        ]
    )
    expected_val = 3.6
    expected_var = 0.35
    expected_err = 0.59161
    expected_relative_err = 0.164335


class TestNoisedValueAverageOfOneValue(TestCase, NoisedValueBaseTestCase):
    v = mean([NoisedValue(val=1.5, err=0.5)])
    expected_val = 1.5
    expected_var = 0.25
    expected_err = 0.5
    expected_relative_err = 0.33333


class TestNoisedValueAverageOfTwoValues(TestCase, NoisedValueBaseTestCase):
    v = mean([NoisedValue(val=1.5, err=0.5), NoisedValue(val=0.9, err=0.1)])
    expected_val = 1.2
    expected_var = 0.065
    expected_err = 0.25495
    expected_relative_err = 0.21246


class TestNoisedValueAverageOfThreeValues(TestCase, NoisedValueBaseTestCase):
    v = mean(
        [
            NoisedValue(val=1.5, err=0.5),
            NoisedValue(val=0.9, err=0.1),
            NoisedValue(val=1.2, err=0.3),
        ]
    )
    expected_val = 1.2
    expected_var = 0.03889
    expected_err = 0.1972
    expected_relative_err = 0.164335


class TestNoisedValueNSigma(TestCase):
    places = 5

    def test_n_sigma(self):
        a = NoisedValue(val=12.62, var=0.36)
        b = NoisedValue(val=12.5, var=1.44)
        expected_n_sigma = 0.08944
        self.assertAlmostEqual(
            expected_n_sigma,
            a.n_sigma(b),
            places=self.places,
            msg="N sigma is different than expected",
        )

    def test_inverse_n_sigma_calculation(self):
        a = NoisedValue(val=12.62, var=0.36)
        b = NoisedValue(val=12.5, var=1.44)
        expected_n_sigma = 0.08944
        self.assertAlmostEqual(
            expected_n_sigma,
            b.n_sigma(a),
            places=self.places,
            msg="N sigma is different than expected",
        )
