"""
You will need to make many changes below. The outline below shows which
documentation pieces you MUST include in your functions in lab
for full credit.
"""
from random import randint



def coord(step_size):
    """
    Generate a random step of size ``step_size`` with equal probability of
    returning a positive or negative step.
    

    Parameters
    ----------

    step_size : float
        Size of step to take.

    Returns
    -------

    float
        A single step, either ``+step_size`` or ``-step_size`` with
        50% probability of each outcome
    """
    # EVERYTHING ABOVE THIS IS REQUIRED
    
    r = randint(0, 1)
    if r == 0:
        step_size = +step_size
    elif r == 1:
        step_size = -step_size
    # Everything below should be replaced by your working code.
    return step_size
