from src.calculator import sum
from src.calculator import div
from src.calculator import mult
from src.calculator import sub

def test_sum()->None: 
    assert sum(3, 5) == 8
    assert sum(10, 9) == 19
    assert sum(20, 50) == 70


def test_div()->None:
    assert div(1, 2) == 0.5
    assert div(10, 2) == 5
    assert div(15, 5) == 3 

def test_mult()->None:
    assert mult(1, 19) == 19
    assert mult(10, 0.2) == 2
    assert mult (0.2, 0.5) == 0.1

def test_sub() -> None:
    assert sub(10, 15) == -5
    assert sub(10.5, 8.5) == 2
    assert sub(10.4, 90.1) == -79.7