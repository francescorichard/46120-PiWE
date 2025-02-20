"""Check some of the functions in arithmetic.
"""
from arithmetic import square
<<<<<<< HEAD
import numpy as np
=======

>>>>>>> cde39cb5b28d1bf339622d109c4ac18430f7e325

def test_square_integer():
    """Test that the square function returns the correct value for an
    integer input."""
    # given
    x = 2
    y_theo = 4
    # when
    y = square(x)
    # then
    assert y == y_theo

<<<<<<< HEAD
def test_square_float():
    """Test that the square function returns the correct value for an
    float input."""
    #given
    x = 3.4
    y_theo = 11.56
    #when
    y = square(x)
    #then
    assert np.isclose(y,y_theo) # this is done because there will be a machine error that need to be eliminated

=======
>>>>>>> cde39cb5b28d1bf339622d109c4ac18430f7e325

# code to execute only if Python is executed directly on this module,
# NOT on import
if __name__ == '__main__':
    test_square_integer()
<<<<<<< HEAD
    test_square_float()
=======
>>>>>>> cde39cb5b28d1bf339622d109c4ac18430f7e325
