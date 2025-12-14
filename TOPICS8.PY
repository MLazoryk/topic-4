# Import Calable type from typing module
# Callable = smth that can be called like a function
from typing import Callable

# Define function 'add' that takes two integers and returns integer
# a: int = parameter 'a' must be integer
# b: int = parameter 'b' must be integer
# -> int = function RETURNS an integer
def add(a: int, b: int) -> int:
    return a + b # Return sum of a and b

