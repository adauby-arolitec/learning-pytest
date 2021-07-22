from maths.basic_calcuations import BasicCalculation
class TestBacisCalculation():
    def test_addition_of_two_positive_numbers(self):
        calculation = BasicCalculation(2,1)
        assert calculation.addition() == 3

    def test_addition_of_positive_and_negative_numbers(self):
        calculation = BasicCalculation(2,-1)
        assert calculation.addition() == 1
    
    def test_addition_of_negative_and_positive_numbers(self):
        assert BasicCalculation(-2,1).addition() == -1

    def test_addition_of_two_negative_numbers(self):
        assert BasicCalculation(-2,-1).addition() == -3
