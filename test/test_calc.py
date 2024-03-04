def test_negatives():
    assert adivb(-10,-5) > 0, "Two negatives should return a positive."



#test 
#import pytest


#assert adivb(-9,3) < 0, "One positive and one negative should return a negative."
#assert adivb(35,7) > 0, "Two positives should return a positive."
#assert isinstance(adivb(5,10), float), "Odd divided by Evens should return a float."
#assert type(adivb(50,10), float), "Larger number divided by lower number should return value > 1."
#assert type(adivb(5,10), float), "Lower number divided by larger number should return value < 1."
#assert adivb(5,2) == 2.5, "5/2 should be 2.5."
#assert adivb(10,3) == pytest.approx(3.33, 0.01), "10/3 should be 3.33."
