import sys
import math
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
    assert math.log(100) == 4.605170185988092

def test_log2():
    assert math.log(100) != 1

def test_square():
    assert square(5) == 25

def test_square2():
    assert square(5) != 20

def test_sin():
    assert sin(90) == 0.8939966636005579

def test_sin2():
    assert sin(90) != 2

def test_cos():
    assert cos(90) == -0.4480736161291701

def test_cos2():
    assert cos(90) != 1

def test_sqrt():
    assert sqrt(25) == 5

def test_sqrt2():
    assert sqrt(25) != 4

def test_percent():
    assert percent(5,6) == 0.30000000000000004

def test_percent2():
    assert percent(5,6) != 1