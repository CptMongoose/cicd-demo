import sys
import math
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from app import add
from app import sub
from app import mult
from app import div
from app import sqaure
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
    assert math.log(100) == 2

def test_log2():
    assert math.log(100) != 1

def test_square():
    assert sqrt(5) == 25

def test_square2():
    assert sqrt(5) != 20

def test_sin():
    assert math.sin(90) == 1

def test_sin2():
    assert math.sin(90) != 2

def test_cos():
    assert math.cos(90) == 0

def test_cos2():
    assert math.cos(90) != 1

def test_sqrt():
    assert math.sqrt(25) == 5

def test_sqrt2():
    assert math.sqrt(25) != 4

def test_percent():
    assert percent(5,6) == 0.3

def test_percent2():
    assert percent(5,6) != 1