from unittest import TestCase

from noised_value import NoisedValue


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
