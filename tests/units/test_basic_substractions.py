from maths.basic_calcuations import BasicCalculation
class TestBacisCalculation():
    def test_substract_of_two_positive_numbers(self):
        substraction = BasicCalculation(3,2)
        assert substraction.substract() == 1

