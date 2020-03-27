from unittest import TestCase

from noised_value import NoisedValue


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
