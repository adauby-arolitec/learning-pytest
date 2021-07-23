import pytest
from maths.basic_calcuations import BasicCalculation


class TestBacisCalculation():
    def test_addition_of_two_positive_numbers(self):
        calculation = BasicCalculation(2, 1)
        assert calculation.addition() == 3

    def test_addition_of_positive_and_negative_numbers(self):
        calculation = BasicCalculation(2, -1)
        assert calculation.addition() == 1

    def test_addition_of_negative_and_positive_numbers(self):
        assert BasicCalculation(-2, 1).addition() == -1

    def test_addition_of_two_negative_numbers(self):
        assert BasicCalculation(-2, -1).addition() == -3

    # coulbyl
    def test_division_of_two_positive_numbers(self):
        calculation = BasicCalculation(2, 2)
        assert calculation.divide() == 1

    def test_division_of_positive_and_negative_numbers(self):
        calculation = BasicCalculation(10, -5)
        assert calculation.divide() == -2

    def test_division_of_negative_and_positive_numbers(self):
        calculation = BasicCalculation(-40, 5)
        assert calculation.divide() == -8

    def test_division_of_two_negative_numbers(self):
        calculation = BasicCalculation(-40, -40)
        assert calculation.divide() == 1

    def test_zero_division_error(self):
        calculation = BasicCalculation(20, 0)
        with pytest.raises(ZeroDivisionError):
            calculation.divide()
