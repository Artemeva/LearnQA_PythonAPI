class TestExample:
    def test_check_math(self):
        a = 5
        b = 9
        expected_sum = 14
        assert a + b == expected_sum, f"sum of variables a and b is not equal to {expected_sum}"
    def test_check_math_fail(self):
        a = 5
        b = 9
        expected_sum = 11
        assert a + b == expected_sum, f"sum of variables a and b is not equal to {expected_sum}"