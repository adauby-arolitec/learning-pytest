
import pytest

from maths.long_time_calculation import LongTimeOperation

#class TestLongTimeOperation():
  
@pytest.mark.integration_test
def test_of_positive_numbers():
    assert LongTimeOperation.calculate(1,1,1) == 2
        
@pytest.mark.integration_test    
def test_of_zero_numbers():
    assert LongTimeOperation.calculate(0,0,0) == 0
        
@pytest.mark.integration_test    
def test_of_positive_and_negative_numbers():
    assert LongTimeOperation.calculate(2,-4,-2) == 10
        
@pytest.mark.integration_test    
def test_of_negative_numbers():
    assert LongTimeOperation.calculate(-2,-4,-2) == 6

        
@pytest.mark.integration_test    
def test_of_mixed_numbers():
    assert LongTimeOperation.calculate(0,3,-2) == -6

      
    


