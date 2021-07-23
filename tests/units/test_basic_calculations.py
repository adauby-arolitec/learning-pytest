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
        assert BasicCalculation(-2,-1).addition() == -3


    def test_multiply_of_two_positive(self):
        assert BasicCalculation(3, 4).multiply() == 12
    
    def test_multiply_of_two_negative(self):
        assert BasicCalculation(-3, -4).multiply() == 12

    def test_multiply_of_negative_and_positive(self):
        assert BasicCalculation(3, -4).multiply() == -12
    
    def test_multiply_of_zero_and_positive(self):
        assert BasicCalculation(0, 4).multiply() == 0
        
    def test_substract_of_two_positive_numbers(self):
        substraction = BasicCalculation(3,2)
        assert substraction.substract() == 1
        
    def test_substract_when_first_number_is_greater_than_second(self):
        substraction = BasicCalculation(7,2)
        assert substraction.substract() == 5
    
    def test_substract_when_second_number_is_greater_than_first(self):
        substraction = BasicCalculation(2,3)
        assert substraction.substract() == -1  
