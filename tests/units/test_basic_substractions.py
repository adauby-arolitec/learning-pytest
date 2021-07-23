from maths.basic_calcuations import BasicCalculation
class TestBacisCalculation():
    def test_substract_of_two_positive_numbers(self):
        substraction = BasicCalculation(3,2)
        assert substraction.substract() == 1
        
    def test_if_first_number_is_greater_than_second(self):
        substraction = BasicCalculation(7,2)
        assert substraction.substract() == 5
    
    def test_if_second_number_is_greater_than_first(self):
        substraction = BasicCalculation(2,3)
        assert substraction.substract() == -1  
