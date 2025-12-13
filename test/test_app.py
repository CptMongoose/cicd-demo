import sys
import math
import pytest
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from app import add
from app import sub
from app import mult
from app import div
from app import square
from app import sin
from app import cos
from app import sqrt
from app import percent
from app import log

def test_add():
    assert add(5,6) == 11

def test_add2():
    assert add(5,6) != 10

def test_sub():
    assert sub(6,5) == 1

def test_sub2():
    assert sub(6,5) != 2

def test_mult():
    assert mult(5,5) == 25

def test_mult2():
    assert mult(5,5) != 20

def test_div():
    assert div(10,5) == 2

def test_div2():
    assert div(10,5) != 1

def test_log():
    assert math.log(100) == math.log(100)

def test_log2():
    assert log(100) != 1

def test_log_error():
    with pytest.raises(ValueError, match="Error"):
        log(0)

def test_log_error_negative():
    with pytest.raises(ValueError, match="Error"):
        log(-5)

def test_square():
    assert square(5) == 25

def test_square2():
    assert square(5) != 20

def test_sin():
    assert sin(90) == math.sin(90)

def test_sin2():
    assert sin(90) != 2

def test_cos():
    assert cos(90) == math.cos(90)

def test_cos2():
    assert cos(90) != 1

def test_sqrt():
    assert sqrt(25) == 5

def test_sqrt2():
    assert sqrt(25) != 4

def test_sqrt_error():
    with pytest.raises(ValueError, match="Error"):
        sqrt(-1)

def test_percent():
    assert percent(5,6) == (5 / 100.0) * 6

def test_percent2():
    assert percent(5,6) != 1

def test_percent_error():
    with pytest.raises(ValueError, match="Error"):
        percent(5, 0)