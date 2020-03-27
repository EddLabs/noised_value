class NoisedValueBaseTestCase:
    places = 5

    def test_value(self):
        self.assertAlmostEqual(
            self.expected_val,
            self.v.val,
            places=self.places,
            msg="Value is different than expected",
        )

    def test_variance(self):
        self.assertAlmostEqual(
            self.expected_var,
            self.v.var,
            places=self.places,
            msg="Variance is different than expected",
        )

    def test_error(self):
        self.assertAlmostEqual(
            self.expected_err,
            self.v.err,
            places=self.places,
            msg="Error is different than expected",
        )

    def test_relative_error(self):
        if self.expected_relative_err is None:
            self.assertRaises(ValueError, getattr, self.v, "relative_err")
        else:
            self.assertAlmostEqual(
                self.expected_relative_err,
                self.v.relative_err,
                places=self.places,
                msg="Relative error is different than expected",
            )
